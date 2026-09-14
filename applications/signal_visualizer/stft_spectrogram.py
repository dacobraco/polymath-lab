import numpy as np
from scipy.signal import chirp, stft
import matplotlib.pyplot as plt

sample_rate = 256
duration = 4

time = np.arange(0, duration, 1 / sample_rate)
signal = chirp(time, f0=10, t1=duration, f1=50, method="linear")

frequencies, segment_times, stft_values = stft(signal, fs=sample_rate, window="hann", nperseg=256, noverlap=192)

stft_magnitude = np.abs(stft_values)
dominant_indices = np.argmax(stft_magnitude, axis=0)
dominant_frequencies = frequencies[dominant_indices]

print("STFT shape:", stft_values.shape)
print("Segment times:", segment_times)
print("Dominant frequencies:", dominant_frequencies)

magnitude_db = 20 * np.log10(stft_magnitude + 1e-12)

figure, axes = plt.subplots(2, 1, figsize=(12, 8))

axes[0].plot(time, signal)
axes[0].set_title("Chirp Signal in the Time Domain")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Amplitude")
axes[0].grid(True)

spectrogram_plot = axes[1].pcolormesh(segment_times, frequencies, magnitude_db, shading="auto", cmap="magma")

axes[1].plot(segment_times, dominant_frequencies, color="cyan", linewidth=2, label="Detected dominant frequency")
axes[1].set_title("STFT Spectrogram")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Frequency [Hz]")
axes[1].set_ylim(0, 60)
axes[1].legend()

figure.colorbar(spectrogram_plot, ax=axes[1], label="Magnitude [dB]")
plt.tight_layout()
plt.show()
