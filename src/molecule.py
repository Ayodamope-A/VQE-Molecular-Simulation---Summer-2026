"""
Defines the hydrogen molecule used in the VQE project.
"""

from openfermion import MolecularData


def create_h2_molecule(
    bond_length: float = 0.74,
    basis: str = "sto-3g",
    multiplicity: int = 1,
    charge: int = 0,
) -> MolecularData:
    """
    Create an H2 molecule.

    Args:
        bond_length: Distance between the hydrogen atoms in angstroms.
        basis: Basis set used for the chemistry calculation.
        multiplicity: Spin multiplicity of H2.
        charge: Total molecular charge.

    Returns:
        MolecularData object describing H2.
    """

    geometry = [
        ("H", (0.0, 0.0, 0.0)),
        ("H", (0.0, 0.0, bond_length)),
    ]

    molecule = MolecularData(
        geometry=geometry,
        basis=basis,
        multiplicity=multiplicity,
        charge=charge,
        description=f"H2_{bond_length:.4f}",
    )

    return molecule
