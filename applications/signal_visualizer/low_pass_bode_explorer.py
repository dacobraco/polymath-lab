import numpy as np
import matplotlib.pyplot as plt

cutoff_frequency = 2  # Hz
frequencies = np.logspace(-1, 3, 1000)
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

first_decade_frequency = 10 * cutoff_frequency
second_decade_frequency = 100 * cutoff_frequency
first_index = np.argmin(np.abs(frequencies - first_decade_frequency))
second_index = np.argmin(np.abs(frequencies - second_decade_frequency))
delta_m = magnitude_db[second_index] - magnitude_db[first_index]
slope = delta_m / np.log10(frequencies[second_index] / frequencies[first_index])

axes[0].scatter(frequencies[first_index], magnitude_db[first_index], color="blue")
axes[0].scatter(frequencies[second_index], magnitude_db[second_index], color="blue")

print("First frequency:", frequencies[first_index], "Hz")
print("Magnitude at first frequency:", magnitude_db[first_index], "dB")
print(f"Second frequency: {frequencies[second_index]}")
print(f"Magnitude at second frequency: {magnitude_db[second_index]}")
print("Measured slope: ", slope, "dB / decade")

for ax in axes:
    ax.grid(True)
    ax.axvline(x=frequencies[cutoff_index], color="red", linestyle="--")

axes[0].axvline(x=frequencies[first_index], color="blue", linestyle="-.")
axes[0].axvline(x=frequencies[second_index], color="blue", linestyle="-.")

plt.tight_layout()
plt.show()
