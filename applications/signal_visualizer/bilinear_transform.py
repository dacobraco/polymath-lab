from scipy.signal import bilinear, freqz
import numpy as np
import matplotlib.pyplot as plt

sampling_frequency = 200.0
analog_cutoff_frequency = 10.0
angular_cutoff_frequency = 2 * np.pi * analog_cutoff_frequency
prewarped_angular_cutoff = 2 * sampling_frequency * np.tan(np.pi * analog_cutoff_frequency / sampling_frequency)
analog_numerator = [angular_cutoff_frequency]
analog_denominator = [1.0, angular_cutoff_frequency]
prewarped_numerator = [prewarped_angular_cutoff]
prewarped_denominator = [1.0, prewarped_angular_cutoff]

digital_numerator, digital_denominator = bilinear(analog_numerator, analog_denominator, fs=sampling_frequency)
prewarped_digital_numerator, prewarped_digital_denominator = bilinear(prewarped_numerator, prewarped_denominator, fs=sampling_frequency)

print("Numerator coefficients:", digital_numerator)
print("Denominator coefficients:", digital_denominator)

frequencies, response = freqz(digital_numerator, digital_denominator, 4096, fs=sampling_frequency)
magnitude = np.abs(response)
print("Frequency range:", frequencies[0], frequencies[-1])

prewarped_frequencies, prewarped_response = freqz(prewarped_digital_numerator, prewarped_digital_denominator, 4096, fs=sampling_frequency)

cutoff_gain = 1 / np.sqrt(2)
cutoff_index = np.argmin(np.abs(magnitude - cutoff_gain))
cutoff_frequency = frequencies[cutoff_index]
print("Digital cutoff frequency:", cutoff_frequency)

prewarped_magnitude = np.abs(prewarped_response)
prewarped_cutoff_index = np.argmin(np.abs(prewarped_magnitude - cutoff_gain))
prewarped_cutoff_frequency = prewarped_frequencies[prewarped_cutoff_index]
print("Prewarped digital cutoff frequency:", prewarped_cutoff_frequency)

target_frequency_index = np.argmin(np.abs(prewarped_frequencies - analog_cutoff_frequency))
gain_at_target_frequency = prewarped_magnitude[target_frequency_index]
print("Gain at 10 Hz:", gain_at_target_frequency)

print("Prewarped digital numerator:", prewarped_digital_numerator)
print("Prewarped digital denominator:", prewarped_digital_denominator)

dc_gain = np.sum(prewarped_digital_numerator) / np.sum(prewarped_digital_denominator)
print("DC gain:", dc_gain)

plt.figure(figsize=(10, 6))

plt.plot(frequencies, magnitude, label="Without prewarping")
plt.plot(prewarped_frequencies, prewarped_magnitude, label="With prewarping")

plt.axvline(analog_cutoff_frequency, linestyle="--", label="Target cutoff: 10 Hz")
plt.axhline(cutoff_gain, linestyle="--", label="Cutoff gain: 1/sqrt(2)")

plt.xlim(0, 30)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.title("Bilinear Transform: Effect of Prewarping")

plt.grid(True)
plt.legend()
plt.tight_layout()

plt.savefig("bilinear_transform_response.png", dpi=150)
plt.show()
