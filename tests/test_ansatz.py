# The steps our team followed to test  
# the ansatz are listed as comments below

import cirq
import numpy as np

from src.ansatz import create_ansatz


# 
# 1. Get the VQE ansatz
# 

ansatz = create_ansatz()

print("VQE Ansatz Circuit:")
print(ansatz)


# 
# 2. Test the circuit
# 

assert isinstance(ansatz, cirq.Circuit)
assert len(ansatz.all_qubits()) == 4
assert len(list(ansatz.all_operations())) == 6
assert cirq.is_parameterized(ansatz)


# 
# 3. Assign parameter values
# 

parameter_values = {
    "theta_0": 0.1,
    "theta_1": 0.2,
    "theta_2": 0.3,
    "theta_3": 0.4
}

resolved_ansatz = cirq.resolve_parameters(
    ansatz,
    parameter_values
)

assert not cirq.is_parameterized(resolved_ansatz)


# 
# 4. Simulate the circuit
# 

simulator = cirq.Simulator()
result = simulator.simulate(resolved_ansatz)

final_state = result.final_state_vector

print("\nFinal state vector:")
print(final_state)


# 
# 5. Check the final state
# 

total_probability = np.sum(np.abs(final_state) ** 2)

assert np.isclose(total_probability, 1.0)

print("\nAll ansatz tests passed!")

