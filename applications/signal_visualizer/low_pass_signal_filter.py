import numpy as np
import matplotlib.pyplot as plt

cutoff_frequency = 10  # Hz
low_frequency = 1  # Hz
high_frequency = 20  # Hz

t = np.linspace(0, 2, 2000)

low_amplitude = 1
high_amplitude = 0.5
low_component = low_amplitude * np.sin(2 * np.pi * low_frequency * t)
high_component = high_amplitude * np.sin(2 * np.pi * high_frequency * t)
input_signal = low_component + high_component

H_low = 1 / (1 + 1j * low_frequency / cutoff_frequency)
H_high = 1 / (1 + 1j * high_frequency / cutoff_frequency)

low_magnitude = np.abs(H_low)
high_magnitude = np.abs(H_high)

print("Low magnitude: ", low_magnitude)
print("High magnitude: ", high_magnitude)

low_output_amplitude = low_magnitude * low_amplitude
high_output_amplitude = high_magnitude * high_amplitude

print("Low output: ", low_output_amplitude)
print("High output: ", high_output_amplitude)

low_phase = np.angle(H_low)
high_phase = np.angle(H_high)

print("Low phase: ", low_phase)
print("High phase: ", high_phase)

filtered_low_component = low_output_amplitude * np.sin(2 * np.pi * low_frequency * t + low_phase)
filtered_high_component = high_output_amplitude * np.sin(2 * np.pi * high_frequency * t + high_phase)

output_signal = filtered_high_component + filtered_low_component

fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(t, input_signal, label="Input signal")
axes[1].plot(t, output_signal, label="Output signal")
axes[0].set_ylabel("Input signal")
axes[1].set_ylabel("Output signal")
axes[1].set_xlabel("Time [s]")
axes[0].set_title("Low pass signal filtering")
axes[1].set_xlim(0, 1)
for ax in axes:
    ax.grid(True)
    ax.legend()

plt.tight_layout()
plt.show()
