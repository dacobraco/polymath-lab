import numpy as np
import matplotlib.pyplot as plt

number_of_samples = 10_000
rng = np.random.default_rng(42)

x_samples = rng.normal(0, 1, number_of_samples)
noise_samples = rng.normal(0, 0.5, number_of_samples)
y_samples = 2 * x_samples + noise_samples

condition_mask = (0.9 < x_samples) & (x_samples < 1.1)
conditional_y_samples = y_samples[condition_mask]

print("Number of conditional Y samples:", len(conditional_y_samples))
print("Mean of all Y samples:", np.mean(y_samples))
print("Mean of conditional Y samples:", np.mean(conditional_y_samples))

plt.figure(figsize=(9, 6))
plt.scatter(x_samples, y_samples, s=10, alpha=0.3)
plt.axvline(0.9, linestyle="--", label="Condition limits")
plt.axvline(1.1, linestyle="--")
plt.title("Joint Distribution of X and Y")
plt.xlabel("X samples")
plt.ylabel("Y samples")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()

plt.figure(figsize=(9, 6))
plt.hist(y_samples, bins=60, density=True, alpha=0.5, label="Y")
plt.hist(conditional_y_samples, bins=30, density=True, alpha=0.7, label="Y | 0.9 < X < 1.1")
plt.title("Marginal and Conditional Distribution of Y")
plt.xlabel("Y")
plt.ylabel("Probability density")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
