import numpy as np
import matplotlib.pyplot as plt

fs = 250_000
duration = 0.05
center_frequency = 100_000_000

t = np.arange(int(fs * duration)) / fs

signal_a = np.exp(1j * 2 * np.pi * 30_000 * t)
signal_b = 0.5 * np.exp(1j * 2 * np.pi * -60_000 * t) * (t < duration / 2)

iq = signal_a + signal_b

np.save("iq_capture.npy", iq)
iq_received = np.load("iq_capture.npy")

print("Number of samples:", len(iq_received))
print("Maximum difference:", np.max(np.abs(iq - iq_received)))

spectrum = np.fft.fftshift(np.fft.fft(iq_received))
frequencies = np.fft.fftshift(np.fft.fftfreq(len(iq_received), d=1/fs))

samples_per_block = 500
iq_blocks = iq_received.reshape(-1, samples_per_block)

block_fft = np.fft.fftshift(np.fft.fft(iq_blocks, axis=1), axes=1)
block_frequencies = np.fft.fftshift(np.fft.fftfreq(samples_per_block, d=1/fs))

waterfall = 20 * np.log10(np.abs(block_fft) + 1e-12)

print(iq_blocks.shape)

plt.figure(figsize=(10, 5))
plt.plot(frequencies / 1000, np.abs(spectrum))
plt.xlabel("Frequency (kHz)")
plt.ylabel("Magnitude")
plt.title("RTL-SDR I/Q Spectrum")
plt.grid(True)
plt.tight_layout()

plt.figure(figsize=(10, 6))
plt.imshow(waterfall, aspect="auto", origin="upper", extent=[block_frequencies[0]/1000, block_frequencies[-1]/1000, duration*1000, 0])
plt.colorbar(label="Magnitude (dB)")
plt.xlabel("Frequency (kHz)")
plt.ylabel("Time (ms)")
plt.title("RTL-SDR Waterfall")
plt.tight_layout()

plt.show()
