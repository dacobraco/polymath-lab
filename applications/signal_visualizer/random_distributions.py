import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import uniform, norm

rng = np.random.default_rng(82)
number_of_samples = 10_000
lower_bound = -1.0
upper_bound = 1.0

uniform_samples = rng.uniform(lower_bound, upper_bound, number_of_samples)
print("Number of samples:", len(uniform_samples))
print("First 10 samples:", uniform_samples[:10])

uniform_x_values = np.linspace(lower_bound, upper_bound, 500)
uniform_theoretical_density = uniform.pdf(uniform_x_values, loc=lower_bound, scale=(upper_bound - lower_bound))
print("First theoretical densities:", uniform_theoretical_density[:5])

plt.hist(uniform_samples, bins=20, density=True, label="Samples", alpha=0.7)
plt.plot(uniform_x_values, uniform_theoretical_density, label="Theoretical PDF")
plt.xlabel("Value")
plt.ylabel("Probability density")
plt.title("Uniform Distribution: Samples vs Theoretical PDF")
plt.legend()
plt.show()

normal_mean = 0.0
normal_standard_deviation = 1.0

normal_samples = rng.normal(normal_mean, normal_standard_deviation, number_of_samples)
print("First 10 normal samples:", normal_samples[:10])

normal_x_values = np.linspace(-4.0, 4.0, 500)
normal_theoretical_density = norm.pdf(normal_x_values, loc=normal_mean, scale=normal_standard_deviation)

plt.hist(normal_samples, bins=40, density=True, alpha=0.7, label="Samples")
plt.plot(normal_x_values, normal_theoretical_density, label="Theoretical PDF")

plt.xlabel("Value")
plt.ylabel("Probability density")
plt.title("Normal Distribution: Samples vs Theoretical PDF")
plt.legend()
plt.show()

cdf_at_upper_bound = norm.cdf(upper_bound, loc=normal_mean, scale=normal_standard_deviation)
cdf_at_lower_bound = norm.cdf(lower_bound, loc=normal_mean, scale=normal_standard_deviation)

probability_between_minus_one_and_one = cdf_at_upper_bound - cdf_at_lower_bound
print("P(-1 <= X <= 1):", probability_between_minus_one_and_one)

inside_interval = (normal_samples >= lower_bound) & (normal_samples <= upper_bound)
number_inside_interval = np.sum(inside_interval)
empirical_probability = number_inside_interval / number_of_samples
print("Empirical P(-1 <= X <= 1):", empirical_probability)
print("Theoretical P(-1 <= X <= 1):", probability_between_minus_one_and_one)

assert np.isclose(empirical_probability, probability_between_minus_one_and_one, atol=0.02)
