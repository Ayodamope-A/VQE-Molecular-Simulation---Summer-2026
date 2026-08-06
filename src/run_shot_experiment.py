# the code contains comments that explains what each
# code segment performs

"""
TEAM, THIS IS THE PROCEDURE FOR RUNNING THIS FILE

1. Activate the project's virtual environment.
2. Run this file before running visualization2.py.
3. Change only shot_counts and trial_number to perform
   a different experiment.
4. This file replaces results/results.csv each time it runs.
"""

from pathlib import Path

import pandas as pd
import numpy as np

from molecule import create_h2_molecule
from hamiltonian import generate_hamiltonian
from exact_solver import (
    get_exact_energy,
    calculate_error
)
from vqe import vqe


# EXPERIMENT SETTINGS
#
# Each value represents the number of measurements
# performed for every measured Hamiltonian term.
#
# Add or remove values to test different shot counts.
# Larger values should produce more consistent results,
# but they will also increase the execution time.

shot_counts = [
    100,
    1000,
    10000,
    100000
]

# This determines how many times each shot count is tested.
#
# More trials produce more reliable averages and standard
# deviations, but they also increase the execution time.
trial_number = 30

# Do not change this list.
# It stores the result from every completed trial.

results = []

# EDIT (08/05/2025) Create a list called "bond_length"

# Create several bond lengths between 0.1 and 2.0 angstroms.
# The third number controls how many bond lengths are tested.
bond_lengths = np.linspace(0.1, 2.0, 10)

# Test every bond length individually.
for bond_length in bond_lengths:

    bond_length = float(bond_length)

    print(f"\nTesting bond length: {bond_length:.4f}")

    # Create H2 using the current bond length.
    molecule = create_h2_molecule(bond_length)

    # Generate a new Hamiltonian for this bond length.
    molecule, qubit_hamiltonian = generate_hamiltonian(
        molecule
    )

    # Calculate the exact energy for this bond length.
    exact_energy = get_exact_energy(molecule)

    # Run every shot count.
    for shots in shot_counts:
        for trial in range(trial_number):

            vqe_energy = vqe(
                qubit_hamiltonian,
                shots
            )

            absolute_error = calculate_error(
                vqe_energy,
                exact_energy
            )

            percent_error = (
                absolute_error
                / abs(exact_energy)
                * 100
            )

            result = {
                "Bond Length": bond_length,
                "Shot Count": shots,
                "Trial": trial + 1,
                "Exact Energy": exact_energy,
                "VQE Energy": vqe_energy,
                "Absolute Error": absolute_error,
                "Percent Error": percent_error
            }

            results.append(result)

            print(
                "Bond Length:",
                round(bond_length, 4),
                "| Shots:",
                shots,
                "| Trial:",
                trial + 1,
                "| VQE Energy:",
                vqe_energy,
                "| Absolute Error:",
                absolute_error
            )


# Create the results folder if needed
Path("results").mkdir(exist_ok=True)

# Save every individual trial.
#
# WARNING: This file is replaced each time the
# experiment runs. Rename or copy an important
# results file before starting another experiment.
experiment_data = pd.DataFrame(results)

experiment_data.to_csv(
    "results/results.csv",
    index=False
)
# Group the trials by shot count.
#
# The mean represents the average result.
# The standard deviation shows how much the trials varied.

summary = experiment_data.groupby(
    ["Bond Length", "Shot Count"]
).agg({
    "Exact Energy": "first",
    "VQE Energy": ["mean", "std"],
    "Absolute Error": ["mean", "std", "min", "max"],
    "Percent Error": ["mean", "std"]
})

# Save the summary using the number of trials
# in the filename.
#
# For example, five trials create:
# results/summary_trial_number5.csv

summary.to_csv(
    f"results/summary_trial_number{trial_number}.csv"
)

# Display the final summary in the terminal.

print("\nSummary:")
print(summary)


print("\nResults saved to results/results.csv")

# Debugging Note to the Team

# This version of the code corrects the previously
# undefined H_sparse and exact_energy variables.
# It also runs VQE inside the loops and passes the
# current shots value.
