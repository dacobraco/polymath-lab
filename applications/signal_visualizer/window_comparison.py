import numpy as np
from scipy.signal import windows
import matplotlib.pyplot as plt

sampling_rate = 64.0
N = 64
frequency = 8.5
amplitude = 3.0

t = np.arange(N) / sampling_rate
signal = amplitude * np.sin(2*np.pi*frequency*t)

rectangular_window = np.ones(N)
hann_window = windows.hann(N, sym=False)
hamming_window = windows.hamming(N, sym=False)
blackman_window = windows.blackman(N, sym=False)

hann_signal = signal * hann_window
rectangular_signal = signal * rectangular_window
hamming_signal = signal * hamming_window
blackman_signal = signal * blackman_window

rectangular_spectrum = np.fft.fft(rectangular_signal)
hann_spectrum = np.fft.fft(hann_signal)
hamming_spectrum = np.fft.fft(hamming_signal)
blackman_spectrum = np.fft.fft(blackman_signal)

rectangular_gain = np.mean(rectangular_window)
hann_gain = np.mean(hann_window)
hamming_gain = np.mean(hamming_window)
blackman_gain = np.mean(blackman_window)

positive_frequencies = np.arange(N//2 + 1) * sampling_rate / N

hann_one_sided = np.abs(hann_spectrum[:N//2 + 1]) / (N * hann_gain)
hann_one_sided[1:-1] *= 2

rectangular_one_sided = np.abs(rectangular_spectrum[:N//2 + 1]) / (N * rectangular_gain)
rectangular_one_sided[1:-1] *= 2

hamming_one_sided = np.abs(hamming_spectrum[:N//2 + 1]) / (N * hamming_gain)
hamming_one_sided[1:-1] *= 2

blackman_one_sided = np.abs(blackman_spectrum[:N//2 + 1]) / (N * blackman_gain)
blackman_one_sided[1:-1] *= 2

print("Rectangular gain:", rectangular_gain)
print("Hann gain:", hann_gain)
print("Hamming gain:", hamming_gain)
print("Blackman gain:", blackman_gain)

epsilon = 1e-12

rectangular_db = 20 * np.log10(rectangular_one_sided / np.max(rectangular_one_sided) + epsilon)
hann_db = 20 * np.log10(hann_one_sided / np.max(hann_one_sided) + epsilon)
hamming_db = 20 * np.log10(hamming_one_sided / np.max(hamming_one_sided) + epsilon)
blackman_db = 20 * np.log10(blackman_one_sided / np.max(blackman_one_sided) + epsilon)

comparison_bin = 15

print("Leakage at 15 Hz:")
print("Rectangular:", rectangular_db[comparison_bin], "dB")
print("Hann:", hann_db[comparison_bin], "dB")
print("Hamming:", hamming_db[comparison_bin], "dB")
print("Blackman:", blackman_db[comparison_bin], "dB")

plt.figure(figsize=(11, 7))

plt.plot(positive_frequencies, rectangular_db, marker="o", label="Rectangular")
plt.plot(positive_frequencies, hann_db, marker="o", label="Hann")
plt.plot(positive_frequencies, hamming_db, marker="o", label="Hamming")
plt.plot(positive_frequencies, blackman_db, marker="o", label="Blackman")

plt.xlim(0, 20)
plt.ylim(-100, 5)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Relative amplitude [dB]")
plt.title("Spectral leakage: window comparison")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
