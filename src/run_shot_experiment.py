import pandas as pd
from vqe import vqe

shot_counts = [100, 500, 1000, 5000, 10000]
trial_number = 3
results = []
vqe_energy = vqe(H_sparse)
percent_error = abs(vqe_energy - exact_energy)


for shots in shot_counts:
    for trial in range(trial_number):

        dictionary = {
            "Shot Count": shot_counts,
            "Trial": trial + 1,
            "Exact Energy": exact_energy,
            "VQE Energy": vqe_energy,
            "Percent Error": percent_error
        }
        results.append(dictionary)
        print("Shot Count:", shots, "Trial:", trial + 1)

experiment_data = pd.DataFrame(results)
experiment_data.to_csv("results/results.csv", index=False)
