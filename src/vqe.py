import numpy as np
import cirq
import pennylane
from scipy.optimize import minimize
from ansatz import create_ansatz

import warnings
warnings.filterwarnings("ignore")


def vqe(H_Sparse):

    def expectation(params):
        resolver = cirq.ParamResolver({str(symbols[i]): params[i] for i in range(4)})
        result = sim.simulate(circuit, resolver)
        psi = result.final_state_vector  # shape: (16,)
        return np.real(psi.conj().T @ (H_Sparse @ psi))

    circuit, symbols = create_ansatz()
    sim = cirq.Simulator()
    
    x0 = np.random.uniform(0, 2*np.pi, 4)
    res = minimize(expectation, x0=x0, method='COBYLA', options={'maxiter': 300})
    return res.fun
    
dataset= pennylane.data.load("qchem", molname="H2")[0]

H_Sparse= pennylane.matrix(dataset.hamiltonian)
# H_Sparse = replace with hamiltonian when whoever's done


print(vqe(H_Sparse))

