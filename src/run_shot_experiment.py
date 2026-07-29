import pandas as pd

shot_counts = [100, 500, 1000, 5000, 10000]
trial_number = 3
results = []
percent_error = abs(vqe_energy - exact_energy)

dictionary = {
    "Shout Count": shot_counts,
    "Trial": trial + 1,
    "Exact Energy": exact_energy,
    "VQE Energy": vqe_energy,
    "Percent Error": percent_error
}

for shots in shot_counts:
    for trial in range(trial_number):
        print("Shot Count:", shots, "Trial:", trial + 1)

 results.append(dictionary)
 df = pd.DataFrame(results)
 df.to_csv("results/results.csv", index=False)
