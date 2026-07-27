import sympy

import cirq


def create_ansatz():
    qubits = cirq.LineQubit.range(4)
    symbols = [sympy.Symbol(f'theta_{i}') for i in range(4)]

    circuit = cirq.Circuit()
    for i in range(4):
        circuit.append(cirq.rx(symbols[i])(qubits[i]))

    for i in range(len(qubits) - 1):
        circuit.append(cirq.CNOT(qubits[i], qubits[i+1]))
    return circuit

print(create_ansatz())