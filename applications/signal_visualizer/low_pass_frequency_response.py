import numpy as np
import matplotlib.pyplot as plt

cutoff_frequency = 2  # Hz
frequencies = np.linspace(0, 20, 1001)
frequency_ratio = frequencies / cutoff_frequency
cutoff_index = np.argmin(np.abs(frequencies - cutoff_frequency))

H = 1 / (1 + 1j * frequency_ratio)

magnitude = np.abs(H)
phase = np.degrees(np.angle(H))

print(f"Cutoff frequency: {frequencies[cutoff_index]} Hz")
print(f"Magnitude at cutoff: {magnitude[cutoff_index]}")
print(f"Phase at cutoff: {phase[cutoff_index]}°")

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(frequencies, magnitude)
axes[1].plot(frequencies, phase)
axes[0].set_ylabel("Magnitude")
axes[1].set_ylabel("Phase [deg]")
axes[1].set_xlabel("Frequency [Hz]")
axes[0].set_title("First-Order Low-Pass Frequency Response")

for ax in axes:
    ax.axvline(x=cutoff_frequency, color="red", linestyle="--")
    ax.grid(True)

plt.tight_layout()
plt.show()
