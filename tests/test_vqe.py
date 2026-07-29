# The Steps we followed to test the vqe are
# commented throughout this python code.



import numpy as np

from src.vqe import vqe


#
# 1. Create a simple test Hamiltonian
#

test_hamiltonian = np.identity(16)


#
# 2. Run the VQE function
#

vqe_energy = vqe(test_hamiltonian)

print("VQE Test Energy:")
print(vqe_energy)


#
# 3. Check the result
#

# Check that the result is a number
assert np.isscalar(vqe_energy)

# Check that the result is not infinity or NaN
assert np.isfinite(vqe_energy)


#
# 4. Check the calculated energy
#

# The identity Hamiltonian always has an energy of 1.
assert np.isclose(vqe_energy, 1.0)


print("\nAll VQE tests passed!")

