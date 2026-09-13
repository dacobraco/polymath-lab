import numpy as np
import matplotlib.pyplot as plt


sampling_frequency = 500
duration = 4

time = np.arange(0, duration, 1 / sampling_frequency)

useful_signal = np.sin(2 * np.pi * 12 * time)
interference = 0.25 * np.sin(2 * np.pi * 60 * time)

signal = useful_signal + interference + 0.75 * np.sin(2 * np.pi * 35 * time)

spectrum = np.fft.fft(signal)

magnitude = np.abs(spectrum)

frequencies = np.fft.fftfreq(len(signal), d=1 / sampling_frequency)

positive_mask = frequencies >= 0

positive_frequencies = frequencies[positive_mask]
positive_magnitude = magnitude[positive_mask]

search_magnitude = positive_magnitude.copy()
search_magnitude[0] = 0

peak_indices = np.argsort(search_magnitude)[-3:][::-1]

dominant_frequencies = positive_frequencies[peak_indices]
dominant_magnitudes = positive_magnitude[peak_indices]

print("Detected dominant frequencies:")

for frequency, peak_magnitude in zip(dominant_frequencies, dominant_magnitudes):
    print(f"{frequency:.2f} Hz, magnitude = {peak_magnitude:.2f}")


plt.figure(figsize=(10, 5))

plt.plot(time, signal)

plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Sampled Signal")
plt.grid(True)
plt.tight_layout()


plt.figure(figsize=(10, 5))

plt.plot(positive_frequencies, positive_magnitude)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.title("DFT Magnitude Spectrum")
plt.xlim(0, 100)
plt.grid(True)
plt.tight_layout()

plt.show()
