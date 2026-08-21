import numpy as np
import matplotlib.pyplot as plt
signal_frequency = 5  # Hz
duration = 1  # s
reference_rate = 2000  # points per second
sample_rates = [40, 12, 10, 8]
nyquist_rate = 2 * signal_frequency
print("Signal frequency:", signal_frequency, "Hz")
print("Nyquist rate:", nyquist_rate, "Hz")
print("Sampling frequencies:", sample_rates)
reference_time = np.arange(0, duration, 1 / reference_rate)
reference_signal = np.sin(2 * np.pi * signal_frequency * reference_time)
fig, axes = plt.subplots(2, 2, figsize=(12, 8), sharex=True, sharey=True)
axes = axes.flatten()
for index, sample_rate in enumerate(sample_rates):
    if sample_rate > nyquist_rate:
        status = "Safe"
    elif sample_rate == nyquist_rate:
        status = "Boundary"
    else:
        status = "Unsafe"
    sample_interval = 1 / sample_rate
    sample_time = np.arange(0, duration, sample_interval)
    sampled_signal = np.sin(2 * np.pi * signal_frequency * sample_time)
    axis = axes[index]
    axis.plot(reference_time, reference_signal, color="tab:blue", label="Continuous-Time Reference")
    axis.plot(sample_time, sampled_signal, marker="o", linestyle="none", color="tab:red", label="Samples")
    axis.set_title(f"{sample_rate} Hz - {status}")
    axis.set_xlabel("Time [s]")
    axis.set_ylabel("Amplitude")
    axis.legend()
    axis.grid(True)
    print(f"{sample_rate} Hz: {status}, {sample_rate / signal_frequency} samples per period, {len(sampled_signal)} total samples")
boundary_rate = nyquist_rate
boundary_time = np.arange(0, duration, 1 / boundary_rate)
zero_phase_samples = np.sin(2 * np.pi * signal_frequency * boundary_time)
shifted_phase_samples = np.sin(2 * np.pi * signal_frequency * boundary_time + np.pi / 2)
print("Boundary samples with phase 0:", zero_phase_samples)
print("Boundary samples with phase pi/2:", shifted_phase_samples)
boundary_fig, boundary_axes = plt.subplots(2, 1, figsize=(10, 6), sharex=True, sharey=True)
boundary_axes[0].stem(boundary_time, zero_phase_samples)
boundary_axes[0].set_title("Nyquist Boundary with Phase 0")
boundary_axes[0].set_ylabel("Amplitude")
boundary_axes[0].grid(True)
boundary_axes[1].stem(boundary_time, shifted_phase_samples)
boundary_axes[1].set_title("Nyquist Boundary with Phase pi/2")
boundary_axes[1].set_xlabel("Time [s]")
boundary_axes[1].set_ylabel("Amplitude")
boundary_axes[1].grid(True)
fig.tight_layout()
boundary_fig.tight_layout()
plt.show()
