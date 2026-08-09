import numpy as np
import matplotlib.pyplot as plt

period = 1
fundamental_frequency = 1 / period
omega_0 = 2 * np.pi * fundamental_frequency

t = np.linspace(-2, 2, 2000)
amp = 4 / np.pi
ideal = np.sign(np.sin(omega_0 * t))


harmonic_limits = [1, 3, 5, 9]
reconstructions = {}

for K in harmonic_limits:
    partial_sum = np.zeros_like(t)

    for k in range(1, K + 1, 2):
        partial_sum += amp / k * np.sin(k * omega_0 * t)

    reconstructions[K] = partial_sum

for i in reconstructions:
    plt.plot(t, reconstructions[i], label=f"K={i}")

plt.plot(t, ideal, label="Ideal", color="black", linestyle="--")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Square-Wave Fourier Reconstruction")
plt.legend()
plt.grid(True)
plt.ylim(-1.5, 1.5)
plt.tight_layout()
plt.show()
