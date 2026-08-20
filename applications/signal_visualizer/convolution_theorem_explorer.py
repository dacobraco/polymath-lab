import numpy as np
import matplotlib.pyplot as plt

example_input = [1, 2, 4, 7]
example_filter = [1, -1]
example_fft_length = len(example_input) + len(example_filter) - 1
example_time_result = np.convolve(example_input, example_filter)
example_input_spectrum = np.fft.fft(example_input, n=example_fft_length)
example_filter_spectrum = np.fft.fft(example_filter, n=example_fft_length)
example_frequency_product = example_input_spectrum * example_filter_spectrum
example_frequency_result = np.real_if_close(np.fft.ifft(example_frequency_product))
example_max_error = np.max(np.abs(example_time_result - example_frequency_result))

print("Time-domain result:", example_time_result)
print("Frequency-domain result:", example_frequency_result)
print("Maximum error:", example_max_error)

sample_rate = 100  # Hz
duration = 2  # s

time = np.arange(0, duration, 1 / sample_rate)
input_signal = np.sin(2 * np.pi * 2 * time) + 0.4 * np.sin(2 * np.pi * 20 * time)
moving_average_filter = np.ones(5) / 5
time_domain_filtered = np.convolve(input_signal, moving_average_filter)
filter_fft_length = len(input_signal) + len(moving_average_filter) - 1
input_spectrum = np.fft.fft(input_signal, n=filter_fft_length)
filter_spectrum = np.fft.fft(moving_average_filter, n=filter_fft_length)
frequency_product = input_spectrum * filter_spectrum
frequency_domain_filtered = np.real_if_close(np.fft.ifft(frequency_product))
filtering_error = np.max(np.abs(time_domain_filtered - frequency_domain_filtered))

print("Input length:", len(input_signal))
print("Filter length:", len(moving_average_filter))
print("Filtered length:", len(time_domain_filtered))
print("Required FFT length:", filter_fft_length)
print("Moving-average filter:", moving_average_filter)
print("Time-domain filtered length:", len(time_domain_filtered))
print("Frequency-domain filtered length:", len(frequency_domain_filtered))
print("Maximum filtering error:", filtering_error)

output_time = np.arange(len(time_domain_filtered)) / sample_rate
absolute_difference = np.abs(time_domain_filtered - frequency_domain_filtered)

fig, axes = plt.subplots(3, 1, figsize=(10, 9))

axes[0].plot(time, input_signal, color="tab:blue", label="Input Signal")
axes[0].set_title("Input Signal with 20 Hz Interference")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Amplitude")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(output_time, time_domain_filtered, color="tab:orange", linewidth=2, label="Time-Domain Convolution")
axes[1].plot(output_time, frequency_domain_filtered, color="tab:green", linestyle="--", linewidth=1.5, label="Frequency-Domain Multiplication")
axes[1].set_title("Time-Domain vs Frequency-Domain Filtering")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Amplitude")
axes[1].legend()
axes[1].grid(True)

axes[2].plot(output_time, absolute_difference, color="tab:red")
axes[2].set_title("Absolute Difference Between Methods")
axes[2].set_xlabel("Time [s]")
axes[2].set_ylabel("Absolute Error")
axes[2].grid(True)

plt.tight_layout()
plt.show()
