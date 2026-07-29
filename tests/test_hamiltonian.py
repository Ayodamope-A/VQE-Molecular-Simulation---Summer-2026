# The Steps we followed to test the hamiltonian are
# commented throughout this python code.


from openfermion import MolecularData, QubitOperator

from src.hamiltonian import generate_hamiltonian


#
# 1. Create an H2 molecule
#

geometry = [
    ("H", (0, 0, 0)),
    ("H", (0, 0, 0.74))
]

molecule = MolecularData(
    geometry=geometry,
    basis="sto-3g",
    multiplicity=1,
    charge=0
)


#
# 2. Generate the Hamiltonian
#

calculated_molecule, qubit_hamiltonian = generate_hamiltonian(
    molecule
)

print("Qubit Hamiltonian:")
print(qubit_hamiltonian)


#
# 3. Test the molecule
#

assert calculated_molecule is not None
assert calculated_molecule.hf_energy is not None
assert calculated_molecule.fci_energy is not None


#
# 4. Test the Hamiltonian
#

assert isinstance(
    qubit_hamiltonian,
    QubitOperator
)

assert len(qubit_hamiltonian.terms) > 0


print("\nHartree-Fock energy:")
print(calculated_molecule.hf_energy)

print("\nExact FCI energy:")
print(calculated_molecule.fci_energy)

print("\nAll Hamiltonian tests passed!")

