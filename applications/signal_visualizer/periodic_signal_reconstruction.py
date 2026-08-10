import numpy as np
import matplotlib.pyplot as plt

harmonic_counts = [1, 3, 5, 20]
theta = np.linspace(-2 * np.pi, 2 * np.pi, 5000)
t_wrapped = (theta + np.pi) % (2 * np.pi) - np.pi
x_ideal = t_wrapped / np.pi

reconstructions = []

for N in harmonic_counts:
    array = np.zeros_like(theta)
    for n in range(1, N + 1):
        array += 2 / np.pi * ((-1) ** (n + 1)) / n * np.sin(n * theta)
    reconstructions.append(array)

rmse_values = []

for N, reconstruction in zip(harmonic_counts, reconstructions):
    error = x_ideal - reconstruction
    squared_error = error ** 2
    mean_squared_error = np.mean(squared_error)
    rmse = np.sqrt(mean_squared_error)
    rmse_values.append(rmse)
    print(f"N = {N}, RMSE = {rmse:.6f}")

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, N, reconstruction, rmse in zip(axes, harmonic_counts, reconstructions, rmse_values):
    ax.plot(theta, x_ideal, label="Ideal Sawtooth")
    ax.plot(theta, reconstruction, label=f"Fourier Reconstruction (N = {N})")
    ax.set_title(f"N = {N}, RMSE = {rmse:.6f}")
    ax.set_xlabel("Angle [rad]")
    ax.set_ylabel("Amplitude")
    ax.set_ylim(-1.2, 1.2)
    ax.grid(True, alpha=0.3)
    ax.legend()

plt.tight_layout()
plt.show()
