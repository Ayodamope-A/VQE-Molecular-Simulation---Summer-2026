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


# Read the raw experiment results
data = pd.read_csv("results/results.csv")

# Detect the number of trials automatically.
#
# This prevents the group from having to manually change
# the graph filename when trial_number changes.
trial_number = int(
    data["Trial"].max()
)

# Calculate the average absolute error and standard
# deviation for every shot count.
#
# The graph's points represent the mean error.
# The error bars represent the standard deviation.
summary = data.groupby(
    "Shot Count"
)["Absolute Error"].agg(
    ["mean", "std"]
)


# Create the graph
plt.errorbar(
    summary.index,
    summary["mean"],
    yerr=summary["std"],
    marker="o",
    capsize=4
)
# Use a logarithmic x-axis because the shot counts
# may range from hundreds to hundreds of thousands.
plt.xscale("log")
plt.xlabel("Number of Shots")
plt.ylabel("Average Absolute Error")
plt.title("Effect of Shot Count on VQE Error")
plt.grid()

# Save the graph using the detected number of trials.
#
# For example, five trials create:
# results/summary_trial_number5.png
graph_filename = (
    f"results/summary_trial_number"
    f"{trial_number}.png"
)

plt.savefig(
    graph_filename,
    bbox_inches="tight"
)


# Display the graph.
plt.show()

print(
    "Graph saved to",
    graph_filename
)



