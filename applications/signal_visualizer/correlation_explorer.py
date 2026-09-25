import numpy as np
import matplotlib.pyplot as plt

sample_num = 10_000
x = np.linspace(-10.0, 10.0, sample_num)
rng = np.random.default_rng(42)

y_clean = 2*x

clean_covariance = np.cov(x, y_clean)
clean_correlation = np.corrcoef(x, y_clean)

print("Clean covariance matrix:")
print(clean_covariance)
print("Clean correlation matrix:")
print(clean_correlation)
print()

base_noise = rng.normal(0, 1, sample_num)
deviations = np.array([0.1, 1.0, 2.0, 5.0, 10.0])

print("Noise experiment:")

for deviation in deviations:
    loop_noise = deviation*base_noise
    loop_y = 2*x + loop_noise
    loop_correlation = np.corrcoef(x, loop_y)

    print(f"Deviation: {deviation}\tCorrelation: {loop_correlation[0, 1]}")

    plt.figure()
    plt.scatter(x, loop_y, s=10, alpha=0.3)
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title(f"Noise std = {deviation}, Correlation = {loop_correlation[0, 1]:.3f}")
    plt.grid()
    plt.show()

print()

positive_y = 2*x + base_noise
positive_correlation = np.corrcoef(x, positive_y)

negative_y = -2*x + base_noise
negative_correlation = np.corrcoef(x, negative_y)

square_y = x**2
square_correlation = np.corrcoef(x, square_y)

print("Positive correlation:", positive_correlation[0, 1])
print("Negative correlation:", negative_correlation[0, 1])
print("Nonlinear correlation:", square_correlation[0, 1])

plt.figure()
plt.scatter(x, positive_y, s=10, alpha=0.3)
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Positive linear relationship, Correlation = {positive_correlation[0, 1]:.3f}")
plt.grid()
plt.show()

plt.figure()
plt.scatter(x, negative_y, s=10, alpha=0.3)
plt.xlabel("x")
plt.ylabel("y")
plt.title(f"Negative linear relationship, Correlation = {negative_correlation[0, 1]:.3f}")
plt.grid()
plt.show()

plt.figure()
plt.scatter(x, square_y, s=10, alpha=0.4)
plt.xlabel("x")
plt.ylabel("x²")
plt.title(f"y = x², Correlation = {square_correlation[0, 1]:.3f}")
plt.grid()
plt.show()
