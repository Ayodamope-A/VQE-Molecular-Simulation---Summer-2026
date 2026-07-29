import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("results/results.csv")

table = df[["shots'. "trial", "exact_energy","vqe_energy", "error"]]

print(table)

average_error = df.groupby("shots")["error"].mean()

plt.plot(df["Shout Count"], df["Percent Error"], marker="x")
plt.xlabel("Number of Shots")
plt.ylabel("Absolute Error")
plt.title("Number of Shots compared with energy error")
plt.show()




