import numpy as np

sampling_rate = 64.0
N = 64
frequency = 8.0
amplitude = 3.0

t = np.arange(N) / sampling_rate

signal = 2.0 + amplitude * np.sin(2*np.pi*frequency*t)

frequency_resolution = sampling_rate / N

print("N:", N)
print("Sampling rate:", sampling_rate)
print("Frequency resolution", frequency_resolution)
print("First 5 samples:", signal[:5])
print("Number of time samples:", len(t))

spectrum = np.fft.fft(signal)
magnitude = np.abs(spectrum)

print("Raw magnitude at bin 8:", magnitude[8])

positive_frequencies = np.arange(N//2 + 1) * frequency_resolution
one_sided_amplitude = magnitude[:N//2 + 1] / N
one_sided_amplitude[1:-1] *= 2

dominant_bin = np.argmax(one_sided_amplitude)
dominant_frequency = positive_frequencies[dominant_bin]
dominant_amplitude = one_sided_amplitude[dominant_bin]

print("Dominant bin:", dominant_bin)
print("Dominant frequency:", dominant_frequency, "Hz")
print("Dominant amplitude:", dominant_amplitude)
