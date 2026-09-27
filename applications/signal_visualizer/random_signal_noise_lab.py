import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

fs = 1000.0
T = 5.0
time = np.arange(0, T, 1/fs)
f = 10.0
A = 1.0
std = 2.0

rng = np.random.default_rng(42)
white_noise = rng.normal(0, std, len(time))
clean_signal = A * np.sin(2*np.pi*f*time)
signal = clean_signal + white_noise

plt.plot(time, clean_signal)
plt.plot(time, signal)
plt.xlim(0, 0.5)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Clean and Noisy Signal")
plt.grid()
plt.show()

frequencies, psd = welch(signal, fs=fs, nperseg=1024)
max_frequency = frequencies[np.argmax(psd)]
print("Max frequency:", max_frequency)

autocorrelation = np.correlate(signal, signal, mode="full")
positive_autocorrelation = autocorrelation[len(time)-1:]

max_peak = np.argmax(positive_autocorrelation[70:130]) + 70
print("Max peak:", max_peak)

seconds = max_peak / fs
print("Seconds:", seconds)

snr_db = 10 * np.log10(np.mean(clean_signal**2) / np.mean(white_noise**2))
print("SNR:", snr_db, "dB")
