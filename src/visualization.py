import pandas as pd
import matplotlib.pyplot as plt


# Read the experiment results
experiment_data = pd.read_csv(
    "results/results.csv"
)

# Display the results table
table = experiment_data[[
    "Shot Count",
    "Trial",
    "Exact Energy",
    "VQE Energy",
    "Absolute Error"
]]

print(table)


# Calculate the average error
average_error = experiment_data.groupby(
    "Shot Count"
)["Absolute Error"].mean()


# Create the graph
plt.plot(
    average_error.index,
    average_error.values,
    marker="x"
)

plt.xlabel("Number of Shots")
plt.ylabel("Average Absolute Error")
plt.title("Shot Count Compared with Energy Error")
plt.grid()
plt.savefig("results/energy_error_graph.png")
plt.show()


### Debugging Note to the Team


# This version of the code corrects the invalid 
# column names, the undefined df variable, and 
# the "Shout Count" spelling error.



