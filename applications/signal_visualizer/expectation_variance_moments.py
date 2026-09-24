import numpy as np

values = np.array([0.0, 2.0, 4.0])

probabilities = np.array([0.25, 0.50, 0.25])
new_probabilities = np.array([0.10, 0.30, 0.60])

sample_counts = [10, 100, 1000, 10_000, 100_000]

rng = np.random.default_rng(42)

theoretical_expectation = np.sum(values * probabilities)
theoretical_second_moment = np.sum(values**2 * probabilities)
theoretical_variance = theoretical_second_moment - theoretical_expectation**2
theoretical_third_central_moment = np.sum((values - theoretical_expectation)**3 * probabilities)
theoretical_fourth_moment = np.sum(values**4 * probabilities)
theoretical_fourth_central_moment = np.sum((values - theoretical_expectation)**4 * probabilities)

new_theoretical_expectation = np.sum(values * new_probabilities)
new_theoretical_second_moment = np.sum(values**2 * new_probabilities)
new_theoretical_variance = new_theoretical_second_moment - new_theoretical_expectation**2
new_theoretical_third_central_moment = np.sum((values - new_theoretical_expectation)**3 * new_probabilities)
new_theoretical_fourth_moment = np.sum(values**4 * new_probabilities)
new_theoretical_fourth_central_moment = np.sum((values - new_theoretical_expectation)**4 * new_probabilities)

print("SYMMETRIC DISTRIBUTION")
print("=" * 100)

for sample_count in sample_counts:
    samples = rng.choice(values, size=sample_count, p=probabilities)

    estimated_expectation = np.mean(samples)
    estimated_variance = np.var(samples)
    second_moment = np.mean(samples**2)
    second_central_moment = np.mean((samples - estimated_expectation)**2)
    third_central_moment = np.mean((samples - estimated_expectation)**3)
    fourth_moment = np.mean(samples**4)
    fourth_central_moment = np.mean((samples - estimated_expectation)**4)

    print("Number of samples:", sample_count)
    print(f"Theoretical expectation: {theoretical_expectation:.6f}\tEstimated expectation: {estimated_expectation:.6f}")
    print(f"Theoretical variance: {theoretical_variance:.6f}\tEstimated variance: {estimated_variance:.6f}")
    print(f"Theoretical second moment: {theoretical_second_moment:.6f}\tEstimated second moment: {second_moment:.6f}")
    print(f"Theoretical third central moment: {theoretical_third_central_moment:.6f}\tEstimated third central moment: {third_central_moment:.6f}")
    print(f"Theoretical fourth moment: {theoretical_fourth_moment:.6f}\tEstimated fourth moment: {fourth_moment:.6f}")
    print(f"Theoretical fourth central moment: {theoretical_fourth_central_moment:.6f}\tEstimated fourth central moment: {fourth_central_moment:.6f}")
    print(f"Second central moment: {second_central_moment:.6f}")
    print()

print("ASYMMETRIC DISTRIBUTION")
print("=" * 100)

for sample_count in sample_counts:
    new_samples = rng.choice(values, size=sample_count, p=new_probabilities)

    estimated_expectation = np.mean(new_samples)
    estimated_variance = np.var(new_samples)
    second_moment = np.mean(new_samples**2)
    second_central_moment = np.mean((new_samples - estimated_expectation)**2)
    third_central_moment = np.mean((new_samples - estimated_expectation)**3)
    fourth_moment = np.mean(new_samples**4)
    fourth_central_moment = np.mean((new_samples - estimated_expectation)**4)

    print("Number of samples:", sample_count)
    print(f"Theoretical expectation: {new_theoretical_expectation:.6f}\tEstimated expectation: {estimated_expectation:.6f}")
    print(f"Theoretical variance: {new_theoretical_variance:.6f}\tEstimated variance: {estimated_variance:.6f}")
    print(f"Theoretical second moment: {new_theoretical_second_moment:.6f}\tEstimated second moment: {second_moment:.6f}")
    print(f"Theoretical third central moment: {new_theoretical_third_central_moment:.6f}\tEstimated third central moment: {third_central_moment:.6f}")
    print(f"Theoretical fourth moment: {new_theoretical_fourth_moment:.6f}\tEstimated fourth moment: {fourth_moment:.6f}")
    print(f"Theoretical fourth central moment: {new_theoretical_fourth_central_moment:.6f}\tEstimated fourth central moment: {fourth_central_moment:.6f}")
    print(f"Second central moment: {second_central_moment:.6f}")
    print()

print("IMPULSIVE NOISE EXPERIMENT")
print("=" * 100)

noise_sample_count = 100_000

normal_noise = rng.normal(loc=0.0, scale=1.0, size=noise_sample_count)

impulsive_noise = normal_noise.copy()

impulse_indices = rng.choice(noise_sample_count, size=20, replace=False)

impulsive_noise[impulse_indices[:10]] = 20.0
impulsive_noise[impulse_indices[10:]] = -20.0

normal_expectation = np.mean(normal_noise)
normal_variance = np.var(normal_noise)
normal_third_central_moment = np.mean((normal_noise - normal_expectation)**3)
normal_fourth_central_moment = np.mean((normal_noise - normal_expectation)**4)

impulsive_expectation = np.mean(impulsive_noise)
impulsive_variance = np.var(impulsive_noise)
impulsive_third_central_moment = np.mean((impulsive_noise - impulsive_expectation)**3)
impulsive_fourth_central_moment = np.mean((impulsive_noise - impulsive_expectation)**4)

print("NORMAL NOISE")
print(f"Expectation: {normal_expectation:.6f}")
print(f"Variance: {normal_variance:.6f}")
print(f"Third central moment: {normal_third_central_moment:.6f}")
print(f"Fourth central moment: {normal_fourth_central_moment:.6f}")
print()

print("NOISE WITH IMPULSES")
print(f"Expectation: {impulsive_expectation:.6f}")
print(f"Variance: {impulsive_variance:.6f}")
print(f"Third central moment: {impulsive_third_central_moment:.6f}")
print(f"Fourth central moment: {impulsive_fourth_central_moment:.6f}")
