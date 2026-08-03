import cirq
import numpy as np

from scipy.optimize import minimize
from openfermion.linalg import get_sparse_operator

from ansatz import create_ansatz


def vqe(qubit_hamiltonian, shots):

    # Create the circuit
    circuit, symbols = create_ansatz()
    simulator = cirq.Simulator()

    # Convert the Hamiltonian to a 16 x 16 matrix
    hamiltonian_matrix = get_sparse_operator(
        qubit_hamiltonian,
        n_qubits=4
    ).toarray()

    # Connect parameter symbols with numerical values
    def get_parameter_values(parameters):
        return {
            symbols[i]: parameters[i]
            for i in range(len(symbols))
        }

    # Calculate energy during optimization
    def expectation(parameters):
        values = get_parameter_values(parameters)

        result = simulator.simulate(
            circuit,
            param_resolver=values
        )

        state = result.final_state_vector

        energy = np.vdot(
            state,
            hamiltonian_matrix @ state
        ).real

        return energy

    # Use the same starting values for every trial
    starting_values = np.zeros(len(symbols))

    optimization = minimize(
        expectation,
        x0=starting_values,
        method="COBYLA",
        options={"maxiter": 300}
    )

    optimized_values = get_parameter_values(
        optimization.x
    )

    resolved_circuit = cirq.resolve_parameters(
        circuit,
        optimized_values
    )

    # Measure the optimized circuit using shots
    measured_energy = 0.0

    for term, coefficient in qubit_hamiltonian.terms.items():

        # Add the identity term directly
        if len(term) == 0:
            measured_energy += coefficient.real
            continue

        measurement_circuit = resolved_circuit.copy()
        measured_qubits = []

        for qubit_number, pauli in term:
            qubit = cirq.LineQubit(qubit_number)
            measured_qubits.append(qubit)

            # Change measurement basis for X
            if pauli == "X":
                measurement_circuit.append(
                    cirq.H(qubit)
                )

            # Change measurement basis for Y
            elif pauli == "Y":
                measurement_circuit.append(
                    cirq.S(qubit) ** -1
                )
                measurement_circuit.append(
                    cirq.H(qubit)
                )

        measurement_circuit.append(
            cirq.measure(
                *measured_qubits,
                key="measurement"
            )
        )

        result = simulator.run(
            measurement_circuit,
            repetitions=shots
        )

        measurements = result.measurements[
            "measurement"
        ]

        eigenvalues = np.prod(
            1 - 2 * measurements,
            axis=1
        )

        term_average = np.mean(eigenvalues)

        measured_energy += (
            coefficient.real * term_average
        )

    return measured_energy
