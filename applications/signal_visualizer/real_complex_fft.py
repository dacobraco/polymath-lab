import numpy as np
import matplotlib.pyplot as plt


sample_rate = 64
duration = 1

number_of_samples = sample_rate * duration
time = np.arange(number_of_samples) / sample_rate

signal = (1.5 * np.cos(2 * np.pi * 8 * time + 0.4) + 0.7 * np.sin(2 * np.pi * 15 * time - 0.2))

full_fft = np.fft.fft(signal)
full_frequencies = np.fft.fftfreq(number_of_samples, d=1 / sample_rate)
positive_coefficient = full_fft[8]
negative_coefficient = full_fft[-8]
conjugated_positive = np.conj(positive_coefficient)

print("Positive frequency:", full_frequencies[8], "Hz")
print("Negative frequency:", full_frequencies[-8], "Hz")
print("FFT at +8 Hz:", positive_coefficient)
print("FFT at -8 Hz:", negative_coefficient)
print("Conjugate of +8 Hz:", conjugated_positive)

positive_magnitude = np.abs(positive_coefficient)
positive_phase = np.angle(positive_coefficient)
recovered_amplitude = 2 * positive_magnitude / number_of_samples

print("Magnitude at +8 Hz:", positive_magnitude)
print("Phase at +8 Hz:", positive_phase, "rad")
print("Recovered amplitude:", recovered_amplitude)

real_fft = np.fft.rfft(signal)
real_frequencies = np.fft.rfftfreq(number_of_samples, d=1/sample_rate)
positive_half_of_full_fft = full_fft[:number_of_samples // 2 + 1]
same_values = np.allclose(real_fft, positive_half_of_full_fft)
largest_difference = np.max(np.abs(real_fft - positive_half_of_full_fft))

print()
print("Number of full FFT values:", len(full_fft))
print("Number of real FFT values:", len(real_fft))
print("Same nonnegative-frequency values:", same_values)
print("Largest difference:", largest_difference)
print("First rFFT frequency:", real_frequencies[0], "Hz")
print("Last rFFT frequency:", real_frequencies[-1], "Hz")

reconstructed_signal = np.fft.irfft(real_fft, n=number_of_samples)
reconstruction_error = np.max(np.abs(signal - reconstructed_signal))

print()
print("Reconstructed samples:", len(reconstructed_signal))
print("Maximum reconstruction error:", reconstruction_error)

iq_signal = np.exp(1j*2*np.pi*8*time)
iq_fft = np.fft.fft(iq_signal)

positive_iq_coefficient = iq_fft[8]
negative_iq_coefficient = iq_fft[-8]

iq_has_conjugate_symmetry = np.allclose(negative_iq_coefficient, np.conj(positive_iq_coefficient))

print()
print("IQ coefficient at +8 Hz:", positive_iq_coefficient)
print("IQ coefficient at -8 Hz:", negative_iq_coefficient)
print("IQ spectrum has conjugate symmetry:", iq_has_conjugate_symmetry)

shifted_frequencies = np.fft.fftshift(full_frequencies)
shifted_real_magnitude = np.fft.fftshift(np.abs(full_fft) / number_of_samples)
shifted_iq_magnitude = np.fft.fftshift(np.abs(iq_fft) / number_of_samples)

figure, axes = plt.subplots(2, 1, figsize=(10, 7))

axes[0].stem(shifted_frequencies, shifted_real_magnitude)
axes[0].set_title("Full FFT of a Real Signal")
axes[0].set_xlabel("Frequency [Hz]")
axes[0].set_ylabel("Magnitude")
axes[0].set_xlim(-32, 32)
axes[0].grid(True)

axes[1].stem(shifted_frequencies, shifted_iq_magnitude)
axes[1].set_title("Full FFT of a Complex IQ Signal")
axes[1].set_xlabel("Frequency [Hz]")
axes[1].set_ylabel("Magnitude")
axes[1].set_xlim(-32, 32)
axes[1].grid(True)

plt.tight_layout()
plt.show()
