import numpy as np
import matplotlib.pyplot as plt

cutoff_frequency = 2  # Hz
frequencies = np.logspace(-1, 2, 1000)
frequency_ratio = frequencies / cutoff_frequency
cutoff_index = np.argmin(np.abs(frequencies - cutoff_frequency))

H = 1 / (1 + frequency_ratio * 1j)

magnitude = np.abs(H)
magnitude_db = 20 * np.log10(magnitude)
phase = np.degrees(np.angle(H))

print(frequencies[cutoff_index])
print(magnitude[cutoff_index])
print(magnitude_db[cutoff_index])
print(phase[cutoff_index])

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].semilogx(frequencies, magnitude_db)
axes[1].semilogx(frequencies, phase)
axes[0].set_ylabel("Magnitude [dB]")
axes[1].set_ylabel("Phase [deg]")
axes[1].set_xlabel("Frequency [Hz]")
axes[0].set_title("Bode explorer")

for ax in axes:
    ax.grid(True)
    ax.axvline(x=cutoff_frequency, color="red", linestyle="--")

plt.tight_layout()
plt.show()
