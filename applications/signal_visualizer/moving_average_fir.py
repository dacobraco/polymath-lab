import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

window_size = 5

filter_coefficients = np.ones(window_size) / window_size

print("Filter coefficients:", filter_coefficients)
print("Sum of coefficients:", np.sum(filter_coefficients))

sample_rate = 100.0
duration = 2.0

time = np.arange(0.0, duration, 1.0 / sample_rate)

clean_signal = np.sin(2.0 * np.pi * 2.0 * time)

print("Number of samples:", len(time))
print("First 5 clean samples:", clean_signal[:5])

random_generator = np.random.default_rng(42)

noise_standard_deviation = 0.5
noise = random_generator.normal(0.0, noise_standard_deviation, size=len(time))

noisy_signal = clean_signal + noise

print("Noise standard deviation:", np.std(noise))
print("First 5 noise samples:", noise[:5])
print("First 5 noisy samples:", noisy_signal[:5])

filtered_signal = np.convolve(noisy_signal, filter_coefficients, mode="same")

print("First 5 filtered samples:", filtered_signal[:5])

filtered_noise = np.convolve(noise, filter_coefficients, mode="same")

half_window = window_size // 2

noise_before = noise[half_window:-half_window]
noise_after = filtered_noise[half_window:-half_window]

print("Noise standard deviation before filtering:", np.std(noise_before))
print("Noise standard deviation after filtering:", np.std(noise_after))
print("Theoretical standard deviation after filtering:", np.std(noise_before) / np.sqrt(window_size))

rmse_before = np.sqrt(np.mean((noisy_signal[half_window:-half_window] - clean_signal[half_window:-half_window]) ** 2))
rmse_after = np.sqrt(np.mean((filtered_signal[half_window:-half_window] - clean_signal[half_window:-half_window]) ** 2))

print("RMSE before filtering:", rmse_before)
print("RMSE after filtering:", rmse_after)

figure, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

axes[0].plot(time, noisy_signal, label="Noisy signal")
axes[0].plot(time, clean_signal, label="Clean signal")
axes[0].set_title("Signal Before Filtering")
axes[0].set_ylabel("Amplitude")
axes[0].grid(True)
axes[0].legend()

axes[1].plot(time, filtered_signal, label="Filtered signal")
axes[1].plot(time, clean_signal, label="Clean signal")
axes[1].set_title("Signal After Moving-Average Filtering")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Amplitude")
axes[1].grid(True)
axes[1].legend()

figure.tight_layout()
plot_path = Path(__file__).with_name("moving_average_fir_filter.png")
figure.savefig(plot_path, dpi=150)
print("Plot saved:", plot_path)
plt.show()

assert np.isclose(np.sum(filter_coefficients), 1.0)
assert np.std(noise_after) < np.std(noise_before)
assert rmse_after < rmse_before

print("Moving-average FIR checks: PASSED")
