import numpy as np
import matplotlib.pyplot as plt

sampling_rate = 64.0
N = 64
amplitude = 3.0

aligned_frequency = 8.0
leaky_frequency = 8.5

t = np.arange(N) / sampling_rate
aligned_signal = amplitude * np.sin(2*np.pi*aligned_frequency*t)
leaky_signal = amplitude * np.sin(2*np.pi*leaky_frequency*t)
frequency_resolution = sampling_rate / N

aligned_spectrum = np.fft.fft(aligned_signal)
leaky_spectrum = np.fft.fft(leaky_signal)

aligned_magnitude = np.abs(aligned_spectrum)
leaky_magnitude = np.abs(leaky_spectrum)

positive_frequencies = np.arange(N//2 + 1) * frequency_resolution

aligned_one_sided = aligned_magnitude[:N//2 + 1] / N
aligned_one_sided[1:-1] *= 2

leaky_one_sided = leaky_magnitude[:N//2 + 1] / N
leaky_one_sided[1:-1] *= 2

print("Aligned 8 Hz case:")
for k in range(5, 13):
    print(positive_frequencies[k], "Hz:", aligned_one_sided[k])

print("\nLeaky 8.5 Hz case:")
for k in range(5, 13):
    print(positive_frequencies[k], "Hz:", leaky_one_sided[k])

aligned_dominant_bin = np.argmax(aligned_one_sided)
aligned_dominant_amplitude = aligned_one_sided[aligned_dominant_bin]

leaky_dominant_bin = np.argmax(leaky_one_sided)
leaky_dominant_amplitude = leaky_one_sided[leaky_dominant_bin]

aligned_dominant_frequency = positive_frequencies[aligned_dominant_bin]
leaky_dominant_frequency = positive_frequencies[leaky_dominant_bin]

print("Aligned dominant frequency:", aligned_dominant_frequency, "Hz")
print("Aligned dominant amplitude:", aligned_dominant_amplitude)

print("Leaky dominant frequency:", leaky_dominant_frequency, "Hz")
print("Leaky dominant amplitude:", leaky_dominant_amplitude)

frequency_error = abs(leaky_frequency - leaky_dominant_frequency)
amplitude_error = abs(amplitude - leaky_dominant_amplitude)
amplitude_error_percent = amplitude_error / amplitude * 100

print("Frequency error:", frequency_error, "Hz")
print("Amplitude error:", amplitude_error)
print("Amplitude error percent:", amplitude_error_percent, "%")

fig, axes = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

axes[0].stem(positive_frequencies, aligned_one_sided)
axes[0].set_title("Aligned signal: 8 Hz")
axes[0].set_ylabel("Amplitude")
axes[0].set_xlim(0, 20)
axes[0].grid(True)

axes[1].stem(positive_frequencies, leaky_one_sided)
axes[1].set_title("Leaky signal: 8.5 Hz")
axes[1].set_xlabel("Frequency [Hz]")
axes[1].set_ylabel("Amplitude")
axes[1].set_xlim(0, 20)
axes[1].grid(True)

plt.tight_layout()
plt.show()
