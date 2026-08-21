import numpy as np
import matplotlib.pyplot as plt

true_frequency = 7  # Hz
sample_rate = 10  # Hz
duration = 1  # s
reference_rate = 2000  # points per second

nyquist_frequency = sample_rate / 2

# This alias calculation is specific to the current k = 1 example.
alias_frequency = np.abs(true_frequency - sample_rate)

sample_interval = 1 / sample_rate

reference_time = np.arange(0, duration, 1 / reference_rate)
sample_time = np.arange(0, duration, sample_interval)

print("True frequency:", true_frequency, "Hz")
print("Sampling frequency:", sample_rate, "Hz")
print("Nyquist frequency:", nyquist_frequency, "Hz")
print("Alias frequency:", alias_frequency, "Hz")
print("Number of samples:", len(sample_time))
print("Sample times:", sample_time)

true_reference = np.cos(2 * np.pi * true_frequency * reference_time)
alias_reference = np.cos(2 * np.pi * alias_frequency * reference_time)

true_samples = np.cos(2 * np.pi * true_frequency * sample_time)
alias_samples = np.cos(2 * np.pi * alias_frequency * sample_time)

print("Matching:", np.allclose(true_samples, alias_samples))

fig, axes = plt.subplots(2, 1, figsize=(10, 7))

axes[0].plot(reference_time, true_reference, color="tab:blue", label="True signal: 7 Hz")
axes[0].stem(sample_time, true_samples, linefmt="k-", markerfmt="ko", basefmt=" ", label="Measured samples")
axes[0].set_title("True Continuous Signal")
axes[0].set_ylabel("Amplitude")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(reference_time, alias_reference, color="tab:orange", label="Alias signal: 3 Hz")
axes[1].stem(sample_time, alias_samples, linefmt="k-", markerfmt="ko", basefmt=" ", label="Same measured samples")
axes[1].set_title("Apparent Aliased Signal")
axes[1].set_xlabel("Time (s)")
axes[1].set_ylabel("Amplitude")
axes[1].legend()
axes[1].grid(True)

fig.suptitle("7 Hz and 3 Hz Produce Identical Samples at a 10 Hz Sampling Rate")
plt.tight_layout()
plt.show()
