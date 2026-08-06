"""
RUNNING THIS FILE

1. Run run_shot_experiment2.py first.
2. Confirm that results/results.csv was created.
3. Run this file to calculate the averages and create
   a graph with error bars.
4. The graph filename automatically includes the
   number of trials found in results.csv.
"""

import pandas as pd
import matplotlib.pyplot as plt


# Read the experiment results
data = pd.read_csv("results/results.csv")

# Detect the number of trials
#
# This prevents the group from having to manually change
# the graph filename when trial_number changes.

trial_number = int(data["Trial"].max())

# Calculate the average and standard deviation for
# every bond-length and shot-count combination

summary = data.groupby(
    ["Bond Length", "Shot Count"],
    as_index=False
).agg(
    exact_energy=("Exact Energy", "first"),
    mean_vqe_energy=("VQE Energy", "mean"),
    std_vqe_energy=("VQE Energy", "std"),
    mean_absolute_error=("Absolute Error", "mean"),
    std_absolute_error=("Absolute Error", "std")
)

# A standard deviation is unavailable when only one trial
# is performed, so replace missing values with zero
summary["std_vqe_energy"] = (
    summary["std_vqe_energy"].fillna(0)
)

# Create the graph
plt.figure(figsize=(10, 6))

# Create one VQE line for each shot count
for shots in sorted(summary["Shot Count"].unique()):

    shot_data = summary[
        summary["Shot Count"] == shots
    ].sort_values("Bond Length")

    plt.errorbar(
        shot_data["Bond Length"],
        shot_data["mean_vqe_energy"],
        yerr=shot_data["std_vqe_energy"],
        marker="o",
        capsize=4,
        label=f"VQE — {shots:,} shots"
    )

# Get one exact-energy value for each bond length
exact_curve = (
    summary
    .drop_duplicates("Bond Length")
    .sort_values("Bond Length")
)

# Add the exact-energy curve
plt.plot(
    exact_curve["Bond Length"],
    exact_curve["exact_energy"],
    color="black",
    linestyle="--",
    marker="x",
    label="Exact Energy"
)

plt.xlabel("H–H Bond Length [in Angstrom]")
plt.ylabel("Energy (Hartree)")
plt.title("H₂ Energy at Different Bond Lengths")
plt.grid(alpha=0.3)
plt.legend()
plt.tight_layout()

# Save the graph
graph_filename = (
    f"results/bond_length_energy_"
    f"{trial_number}_trials.png"
)

plt.savefig(
    graph_filename,
    dpi=300,
    bbox_inches="tight"
)

plt.show()

print("Graph saved to", graph_filename)
