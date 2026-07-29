"""
Provides the exact reference energy for H2 and computes VQE error.
"""


def get_exact_energy(molecule):
    """
    Returns the exact Full Configuration Interaction (FCI)
    energy calculated by PySCF.
    """

    if molecule.fci_energy is None:
        raise ValueError(
            "FCI energy has not been calculated."
        )

    return molecule.fci_energy


def calculate_error(vqe_energy, exact_energy):
    """
    Returns the absolute error between
    the VQE energy and the exact energy.
    """

    return abs(vqe_energy - exact_energy)
