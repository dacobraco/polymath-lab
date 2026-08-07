import numpy as np
import matplotlib.pyplot as plt

cutoff_frequency = 2  # Hz
frequencies = np.logspace(-1, 3, 1000)
ratio = frequencies / cutoff_frequency

H_high = 1j * ratio / (1 + 1j * ratio)
H_low = 1 / (1 + 1j * ratio)

high_magnitude = np.abs(H_high)
high_magnitude_db = 20 * np.log10(high_magnitude)
low_magnitude = np.abs(H_low)
low_magnitude_db = 20 * np.log10(low_magnitude)
high_phase = np.degrees(np.angle(H_high))
cutoff_index = np.argmin(np.abs(frequencies - cutoff_frequency))

power_sum = high_magnitude ** 2 + low_magnitude ** 2
is_complementary = np.allclose(power_sum, 1)

print("Cutoff frequency:", frequencies[cutoff_index])
print("Cutoff magnitude:", high_magnitude[cutoff_index])
print("Cutoff magnitude in dB:", high_magnitude_db[cutoff_index])
print("Cutoff phase:", high_phase[cutoff_index])
print("Complementary magnitude responses:", is_complementary)

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].semilogx(frequencies, high_magnitude_db, label="High-pass")
axes[0].semilogx(frequencies, low_magnitude_db, label="Low-pass")
axes[0].legend()
axes[1].semilogx(frequencies, high_phase)
axes[0].set_ylabel("Magnitude [dB]")
axes[1].set_ylabel("Phase [deg]")
axes[1].set_xlabel("Frequency [Hz]")
axes[0].set_title("First-Order Low-Pass and High-Pass Bode Plot")

for ax in axes:
    ax.grid(True)
    ax.axvline(x=cutoff_frequency, color="red", linestyle="--")

plt.tight_layout()
plt.show()
