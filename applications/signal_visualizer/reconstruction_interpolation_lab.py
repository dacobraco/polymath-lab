import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


signal_frequency = 3  # Hz
sample_rate = 12  # Hz
reference_rate = 2000  # points per second
duration = 1  # s

sample_interval = 1 / sample_rate
nyquist_rate = 2 * signal_frequency

t_reference = np.arange(0, duration, 1 / reference_rate)
x_reference = np.sin(2 * np.pi * signal_frequency * t_reference)

t_samples = np.arange(0, duration, sample_interval)
x_samples = np.sin(2 * np.pi * signal_frequency * t_samples)

zoh_function = interp1d(t_samples, x_samples, kind="previous", bounds_error=False, fill_value=(x_samples[0], x_samples[-1]))
linear_function = interp1d(t_samples, x_samples, kind="linear", bounds_error=False, fill_value=(x_samples[0], x_samples[-1]))

x_zoh = zoh_function(t_reference)
x_linear = linear_function(t_reference)

x_sinc = np.zeros(len(t_reference))

for sample_index in range(len(t_samples)):
    normalized_distance = (t_reference - t_samples[sample_index]) / sample_interval
    kernel = x_samples[sample_index] * np.sinc(normalized_distance)
    x_sinc = x_sinc + kernel

sinc_at_sample_times = np.zeros(len(t_samples))

for sample_index in range(len(t_samples)):
    normalized_distance = (t_samples - t_samples[sample_index]) / sample_interval
    kernel = x_samples[sample_index] * np.sinc(normalized_distance)
    sinc_at_sample_times = sinc_at_sample_times + kernel

sample_reconstruction_error = np.max(np.abs(x_samples - sinc_at_sample_times))

zoh_rmse = np.sqrt(np.mean((x_reference - x_zoh) ** 2))
linear_rmse = np.sqrt(np.mean((x_reference - x_linear) ** 2))
sinc_rmse = np.sqrt(np.mean((x_reference - x_sinc) ** 2))

print("Signal frequency:", signal_frequency, "Hz")
print("Sampling frequency:", sample_rate, "Hz")
print("Nyquist rate:", nyquist_rate, "Hz")
print("Sampling interval:", sample_interval, "s")
print("Number of samples:", len(t_samples))
print("Samples per period:", sample_rate / signal_frequency)
print("Maximum sinc error at sample times:", sample_reconstruction_error)
print("ZOH RMSE:", zoh_rmse)
print("Linear RMSE:", linear_rmse)
print("Sinc RMSE:", sinc_rmse)

fig, axes = plt.subplots(4, 1, figsize=(11, 12), sharex=True, sharey=True)

axes[0].plot(t_reference, x_reference, color="tab:blue", label="Original Signal")
axes[0].plot(t_samples, x_samples, marker="o", linestyle="none", color="tab:red", label="Samples")
axes[0].set_title("Original Signal and Samples")

axes[1].plot(t_reference, x_reference, color="tab:blue", linestyle="--", label="Original Signal")
axes[1].plot(t_reference, x_zoh, color="tab:orange", label="Zero-Order Hold")
axes[1].plot(t_samples, x_samples, marker="o", linestyle="none", color="tab:red", label="Samples")
axes[1].set_title("Zero-Order Hold Reconstruction")

axes[2].plot(t_reference, x_reference, color="tab:blue", linestyle="--", label="Original Signal")
axes[2].plot(t_reference, x_linear, color="tab:green", label="Linear Interpolation")
axes[2].plot(t_samples, x_samples, marker="o", linestyle="none", color="tab:red", label="Samples")
axes[2].set_title("Linear Reconstruction")

axes[3].plot(t_reference, x_reference, color="tab:blue", linestyle="--", label="Original Signal")
axes[3].plot(t_reference, x_sinc, color="tab:purple", label="Sinc Interpolation")
axes[3].plot(t_samples, x_samples, marker="o", linestyle="none", color="tab:red", label="Samples")
axes[3].set_title("Sinc Reconstruction")
axes[3].set_xlabel("Time [s]")

for axis in axes:
    axis.set_ylabel("Amplitude")
    axis.legend()
    axis.grid(True)

plt.tight_layout()
plt.show()