import pandas as pd
import matplotlib.pyplot as plt

experiment_data = pd.read_csv("results/results.csv")

table = experiment_data[["shots'. "trial", "exact_energy","vqe_energy", "error"]]

print(table)

average_error = experiment_data.groupby("shots")["error"].mean()

plt.plot(experiment_data["Shout Count"], df["Percent Error"], marker="x")
plt.xlabel("Number of Shots")
plt.ylabel("Absolute Error")
plt.title("Number of Shots compared with energy error")
plt.show()




