import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(-3, 3, 3001)
frequencies = np.linspace(-10, 10, 3001)

tau_values = [0.25, 0.5, 1, 2]

fig, axes = plt.subplots(len(tau_values), 2, figsize=(10, 10))

for i, tau in enumerate(tau_values):
    x = np.where(np.abs(t) <= tau / 2, 1.0, 0.0)
    X = tau * np.sinc(frequencies * tau)
    bandwidth = 1 / tau

    axes[i, 0].plot(t, x)
    axes[i, 1].plot(frequencies, X)

    axes[i, 1].axvline(x=bandwidth, color="red")
    axes[i, 1].axvline(x=-bandwidth, color="red")

    axes[i, 0].set_title(f"Pulse width = {tau} s")
    axes[i, 1].set_title(f"Bandwidth = {bandwidth} Hz")

    axes[i, 0].set_ylabel("Amplitude")
    axes[i, 1].set_ylabel("Amplitude")

    axes[i, 0].grid(True)
    axes[i, 1].grid(True)

axes[-1, 0].set_xlabel("Time [s]")
axes[-1, 1].set_xlabel("Frequency [Hz]")

plt.tight_layout()
plt.show()
