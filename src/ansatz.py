import sympy

import cirq


def create_ansatz():
    qubits = cirq.LineQubit.range(4)
    symbols = [sympy.Symbol(f'theta_{i}') for i in range(8)]

    circuit = cirq.Circuit()
    circuit.append(cirq.X(qubits[0]))
    circuit.append(cirq.X(qubits[1]))
    
    for x in range(2):
            
        for i in range(4):
            circuit.append(cirq.ry(symbols[x*4+i])(qubits[i]))
    
        circuit.append(cirq.CNOT(qubits[0], qubits[1]))
        circuit.append(cirq.CNOT(qubits[0], qubits[2]))
        circuit.append(cirq.CNOT(qubits[1], qubits[2]))
        circuit.append(cirq.CNOT(qubits[0], qubits[3]))
        circuit.append(cirq.CNOT(qubits[1], qubits[3]))
        circuit.append(cirq.CNOT(qubits[2], qubits[3]))
        
    return circuit, symbols


circuit, symbols = create_ansatz()
noise = cirq.depolarize(0.01)
noisy_circuit = circuit.with_noise(noise)

print(noisy_circuit)
