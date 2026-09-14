import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import periodogram, welch


sample_rate = 256
duration = 4
signal_frequency = 8
signal_amplitude = 4

number_of_samples = sample_rate * duration
time = np.arange(number_of_samples) / sample_rate

signal = signal_amplitude * np.sin(2 * np.pi * signal_frequency * time)

frequency_resolution = sample_rate / number_of_samples

theoretical_power = signal_amplitude**2 / 2
measured_power = np.mean(signal**2)

fft_values = np.fft.rfft(signal)
frequencies = np.fft.rfftfreq(number_of_samples, d=1 / sample_rate)

amplitude_spectrum = 2 * np.abs(fft_values) / number_of_samples
amplitude_spectrum[0] /= 2
amplitude_spectrum[-1] /= 2

energy_spectrum = np.abs(fft_values)**2 / number_of_samples
energy_spectrum[1:-1] *= 2

time_domain_energy = np.sum(signal**2)
frequency_domain_energy = np.sum(energy_spectrum)

psd_frequencies, psd_values = periodogram(signal, fs=sample_rate, window="boxcar", scaling="density")

psd_resolution = psd_frequencies[1] - psd_frequencies[0]
clean_power_from_psd = np.sum(psd_values) * psd_resolution


random_generator = np.random.default_rng(42)
noise = random_generator.normal(0, 3, number_of_samples)
noisy_signal = signal + noise

periodogram_frequencies, periodogram_psd = periodogram(noisy_signal, fs=sample_rate, window="boxcar", scaling="density")

welch_frequencies, welch_psd = welch(
    noisy_signal,
    fs=sample_rate,
    window="hann",
    nperseg=256,
    noverlap=128,
    scaling="density"
)

periodogram_resolution = (periodogram_frequencies[1] - periodogram_frequencies[0])
welch_resolution = (welch_frequencies[1] - welch_frequencies[0])
periodogram_power = (np.sum(periodogram_psd) * periodogram_resolution)
welch_power = (np.sum(welch_psd) * welch_resolution)

dominant_index = np.argmax(amplitude_spectrum)
dominant_frequency = frequencies[dominant_index]
measured_amplitude = amplitude_spectrum[dominant_index]


print("Detected frequency:", dominant_frequency, "Hz")
print("Measured amplitude:", measured_amplitude)
print("Theoretical mean-square power:", theoretical_power)
print("Measured mean-square power:", measured_power)
print("Time-domain energy:", time_domain_energy)
print("Frequency-domain energy:", frequency_domain_energy)
print("Clean power from PSD:", clean_power_from_psd)

print()
print("Noisy signal power:", np.mean(noisy_signal**2))
print("Power from periodogram:", periodogram_power)
print("Power from Welch PSD:", welch_power)
print("Periodogram resolution:", periodogram_resolution, "Hz")
print("Welch resolution:", welch_resolution, "Hz")


figure, axes = plt.subplots(2, 2, figsize=(13, 8))

axes[0, 0].plot(time, signal, label="Clean signal")
axes[0, 0].plot(time, noisy_signal, alpha=0.45, label="Signal with noise")
axes[0, 0].set_title("Signal in the Time Domain")
axes[0, 0].set_xlabel("Time [s]")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].set_xlim(0, 1)
axes[0, 0].legend()
axes[0, 0].grid(True)

axes[0, 1].stem(frequencies, amplitude_spectrum)
axes[0, 1].set_title("Amplitude Spectrum")
axes[0, 1].set_xlabel("Frequency [Hz]")
axes[0, 1].set_ylabel("Amplitude")
axes[0, 1].set_xlim(0, 30)
axes[0, 1].grid(True)

axes[1, 0].stem(frequencies, energy_spectrum)
axes[1, 0].set_title("Energy Spectrum")
axes[1, 0].set_xlabel("Frequency [Hz]")
axes[1, 0].set_ylabel("Energy")
axes[1, 0].set_xlim(0, 30)
axes[1, 0].grid(True)

axes[1, 1].semilogy(periodogram_frequencies, periodogram_psd, alpha=0.6, label="Periodogram")
axes[1, 1].semilogy(welch_frequencies, welch_psd, linewidth=2, label="Welch")

axes[1, 1].set_title("PSD of the Noisy Signal")
axes[1, 1].set_xlabel("Frequency [Hz]")
axes[1, 1].set_ylabel("PSD [amplitude²/Hz]")
axes[1, 1].set_xlim(0, 30)
axes[1, 1].legend()
axes[1, 1].grid(True)

plt.tight_layout()
plt.show()
