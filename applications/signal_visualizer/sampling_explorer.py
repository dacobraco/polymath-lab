import numpy as np
import matplotlib.pyplot as plt

signal_frequency = 5  # Hz
sample_rate = 40  # Hz
duration = 1  # s
reference_rate = 2000  # points per second

sample_interval = 1 / sample_rate

reference_time = np.arange(0, duration, 1 / reference_rate)
sample_time = np.arange(0, duration, sample_interval)

print("Signal frequency:", signal_frequency, "Hz")
print("Sampling frequency:", sample_rate, "Hz")
print("Sampling interval:", sample_interval, "s")
print("Reference points:", len(reference_time))
print("Number of samples:", len(sample_time))
print("First sample times:", sample_time[:5])

reference_signal = np.sin(2 * np.pi * signal_frequency * reference_time)
sampled_signal = np.sin(2 * np.pi * signal_frequency * sample_time)
sample_indices = np.arange(len(sampled_signal))

print("First sample index:", sample_indices[0])
print("Last sample index:", sample_indices[-1])

samples_per_period = sample_rate / signal_frequency

print("Samples per period:", samples_per_period)
print("First sample values:", sampled_signal[:5])

fig, axes = plt.subplots(2, 1, figsize=(10, 7))

axes[0].plot(reference_time, reference_signal, color="tab:blue", label="Continuous-Time Reference")
axes[0].plot(sample_time, sampled_signal, marker="o", linestyle="none", color="tab:red", label="Sampled Values")
axes[0].set_title("Continuous-Time Reference Signal")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Amplitude")
axes[0].legend()
axes[0].grid(True)

axes[1].stem(sample_indices, sampled_signal, label="Discrete-Time Samples")
axes[1].set_title("Discrete-Time Samples")
axes[1].set_xlabel("Sample Index n")
axes[1].set_ylabel("Amplitude")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
