import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

sample_rate = 200.0
duration = 10.0
signal_frequency = 10.0

time = np.arange(0, duration, 1 / sample_rate)

rng = np.random.default_rng(42)
noise = rng.normal(0, 0.5, len(time))

signal = np.sin(2 * np.pi * signal_frequency * time) + noise
centered_signal = signal - np.mean(signal)

autocorrelation = np.correlate(centered_signal, centered_signal, mode="full")
autocorrelation = autocorrelation / len(centered_signal)

lags = np.arange(-len(centered_signal) + 1, len(centered_signal))
lags_seconds = lags / sample_rate

shifted_autocorrelation = np.fft.ifftshift(autocorrelation)
wk_psd = np.real(np.fft.fft(shifted_autocorrelation)) / sample_rate

wk_frequencies = np.fft.fftfreq(len(autocorrelation), d=1 / sample_rate)

wk_frequencies = np.fft.fftshift(wk_frequencies)
wk_psd = np.fft.fftshift(wk_psd)

positive_mask = wk_frequencies >= 0

wk_frequencies_positive = wk_frequencies[positive_mask]
wk_psd_positive = wk_psd[positive_mask]

wk_psd_positive[1:] *= 2
wk_psd_positive = np.maximum(wk_psd_positive, 0)

welch_frequencies, welch_psd = welch(centered_signal, fs=sample_rate, nperseg=512, scaling="density")

wk_peak_index = np.argmax(wk_psd_positive)
welch_peak_index = np.argmax(welch_psd)

wk_peak_frequency = wk_frequencies_positive[wk_peak_index]
welch_peak_frequency = welch_frequencies[welch_peak_index]

print("Expected frequency:", signal_frequency, "Hz")
print("Wiener-Khinchin peak:", wk_peak_frequency, "Hz")
print("Welch PSD peak:", welch_peak_frequency, "Hz")
print("Signal variance:", np.var(centered_signal))

wk_power = np.trapezoid(wk_psd_positive, wk_frequencies_positive)
welch_power = np.trapezoid(welch_psd, welch_frequencies)

print("Power from Wiener-Khinchin PSD:", wk_power)
print("Power from Welch PSD:", welch_power)

plt.figure()
plt.plot(time, signal)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("10 Hz sinusoid with noise")
plt.xlim(0, 2)
plt.grid()

positive_lag_mask = (lags_seconds >= 0) & (lags_seconds <= 1)

plt.figure()
plt.plot(lags_seconds[positive_lag_mask], autocorrelation[positive_lag_mask])
plt.xlabel("Lag [s]")
plt.ylabel("Autocorrelation")
plt.title("Autocorrelation")
plt.grid()

plt.figure()
plt.plot(wk_frequencies_positive, wk_psd_positive, label="FFT of autocorrelation")
plt.plot(welch_frequencies, welch_psd, label="Welch PSD")
plt.xlabel("Frequency [Hz]")
plt.ylabel("PSD [power/Hz]")
plt.title("Wiener-Khinchin theorem")
plt.xlim(0, 50)
plt.legend()
plt.grid()

plt.show()
