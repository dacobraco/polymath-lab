import numpy as np
import matplotlib.pyplot as plt

periods = [2, 4, 8, 16]
pulse_width = 1
frequencies = np.linspace(-5, 5, 2000)

continuous_spectrum = pulse_width * np.sinc(frequencies * pulse_width)

fig, axes = plt.subplots(2, 2, figsize=(12, 8))
axes = axes.flatten()

for ax, T in zip(axes, periods):
    k = np.arange(-5 * T, 5 * T + 1)
    harmonic_frequencies = k / T

    coefficients = (pulse_width / T) * np.sinc(pulse_width * harmonic_frequencies)
    line_heights = T * coefficients
    ax.plot(frequencies, continuous_spectrum, color="red")
    ax.stem(harmonic_frequencies, line_heights)
    ax.set_title(f"T = {T} s, Δf = {1 / T:.3f} Hz")
    ax.set_xlabel("Frequency [Hz]")
    ax.set_ylabel(r"Scaled Amplitude ($T C_k$)")
    ax.grid(True)
    ax.set_xlim(-5, 5)

plt.tight_layout()
plt.show()
