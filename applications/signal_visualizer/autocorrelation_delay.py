import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks

sampling_frequency = 100.0
signal_frequency = 7.0
noise_std = 1.5

t = np.arange(0, 10, 1 / sampling_frequency)

clean_signal = np.sin(2 * np.pi * signal_frequency * t)

rng = np.random.default_rng(42)
noise = rng.normal(0, noise_std, len(clean_signal))

noisy_signal = clean_signal + noise

autocorrelation = np.correlate(noisy_signal, noisy_signal, mode="full")

number_of_samples = len(noisy_signal)
zero_lag_index = number_of_samples - 1

positive_autocorrelation = autocorrelation[zero_lag_index:]
lags = np.arange(len(positive_autocorrelation))

normalized_positive_autocorrelation = positive_autocorrelation / positive_autocorrelation[0]

peak_indices, properties = find_peaks(normalized_positive_autocorrelation[1:], height=0.05, prominence=0.15, distance=5)

detected_lags = peak_indices + 1

print("Noise std:", noise_std)
print("Found lags:", detected_lags)

if len(detected_lags) >= 2:
    peak_spacings = np.diff(detected_lags)
    estimated_lag = np.mean(peak_spacings)

    estimated_period = estimated_lag / sampling_frequency
    estimated_frequency = sampling_frequency / estimated_lag

    print("Peak spacings:", peak_spacings)
    print("Estimated lag from peak spacing:", estimated_lag, "samples")
    print("Estimated period:", estimated_period, "s")
    print("Estimated frequency:", estimated_frequency, "Hz")
elif len(detected_lags) == 1:
    estimated_lag = detected_lags[0]
    estimated_period = estimated_lag / sampling_frequency
    estimated_frequency = sampling_frequency / estimated_lag

    print("Only one peak detected.")
    print("Estimated lag:", estimated_lag, "samples")
    print("Estimated period:", estimated_period, "s")
    print("Estimated frequency:", estimated_frequency, "Hz")
else:
    print("Period not detected.")

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

axes[0].plot(t, clean_signal, label="Clean signal")
axes[0].plot(t, noisy_signal, label="Noisy signal", alpha=0.7)
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Amplitude")
axes[0].set_title(f"Signal frequency = {signal_frequency} Hz, noise std = {noise_std}")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(lags, normalized_positive_autocorrelation, label="Autocorrelation")

if len(detected_lags) > 0:
    axes[1].plot(detected_lags, normalized_positive_autocorrelation[detected_lags], "o", label="Detected peaks")

axes[1].set_xlim(0, 100)
axes[1].set_xlabel("Lag [samples]")
axes[1].set_ylabel("Normalized autocorrelation")
axes[1].set_title("Autocorrelation and detected peaks")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
