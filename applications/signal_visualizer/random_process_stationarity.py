import numpy as np

numbers_of_samples = np.array([10, 100, 1000, 10000])
time_indices = np.array([10, 100, 500, 900])

number_of_realizations = 1000
samples_per_realization = 1000

rng = np.random.default_rng(42)

time_noise = rng.normal(0, 1, numbers_of_samples[-1])

print("TIME AVERAGES")

for number_of_samples in numbers_of_samples:
    current_samples = time_noise[:number_of_samples]

    time_mean = np.mean(current_samples)
    time_variance = np.var(current_samples)

    print(
        f"N: {number_of_samples}\t"
        f"Mean: {time_mean}\t"
        f"Variance: {time_variance}"
    )

ensemble_noise = rng.normal(0, 1, (number_of_realizations, samples_per_realization))

print("\nENSEMBLE AVERAGES")

for n in time_indices:
    ensemble_at_n = ensemble_noise[:, n]

    ensemble_mean = np.mean(ensemble_at_n)
    ensemble_variance = np.var(ensemble_at_n)

    print(
        f"n: {n}\t"
        f"Mean: {ensemble_mean}\t"
        f"Variance: {ensemble_variance}"
    )
