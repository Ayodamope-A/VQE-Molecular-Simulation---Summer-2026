"""
Generates the Hamiltonian for the H2 molecule.
"""

from openfermion.transforms import jordan_wigner
from openfermionpyscf import run_pyscf


def generate_hamiltonian(molecule):
    """
    Runs the PySCF calculation and converts the
    molecular Hamiltonian into a qubit Hamiltonian.
    """

    molecule = run_pyscf(
        molecule,
        run_scf=True,
        run_fci=True
    )

    # Create the molecular Hamiltonian
    molecular_hamiltonian = molecule.get_molecular_hamiltonian()

    # Convert to a qubit Hamiltonian
    qubit_hamiltonian = jordan_wigner(
        molecular_hamiltonian
    )

    return molecule, qubit_hamiltonian
