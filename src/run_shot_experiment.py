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
trial_number = 5

# Do not change this list.
# It stores the result from every completed trial.

results = []


# Create the H2 molecule.
# The molecular settings are defined in molecule.py.
molecule = create_h2_molecule()

# Run PySCF and convert the molecular Hamiltonian
# into a qubit Hamiltonian.
molecule, qubit_hamiltonian = (
    generate_hamiltonian(molecule)
)


# Get the exact FCI energy used as the reference value.
exact_energy = get_exact_energy(molecule)


# Run each shot-count experiment
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
            "Shot Count": shots,
            "Trial": trial + 1,
            "Exact Energy": exact_energy,
            "VQE Energy": vqe_energy,
            "Absolute Error": absolute_error,
            "Percent Error": percent_error
        }

        results.append(result)

        print(
            "Shots:",
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
    "Shot Count"
).agg({
    "VQE Energy": ["mean", "std"],
    "Absolute Error": ["mean", "std", "min", "max"]
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
