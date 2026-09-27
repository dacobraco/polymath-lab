import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import welch

fs = 1000.0
duration = 5.0
time = np.arange(0, duration, 1/fs)
sample_number = len(time)

rng = np.random.default_rng(42)

white_noise = rng.normal(0, 1, sample_number)

rfft_frequencies = np.fft.rfftfreq(sample_number, d=1/fs)
white_rfft = np.fft.rfft(white_noise)

def colored_noise(alpha):
    scale = np.zeros_like(rfft_frequencies)
    mask = rfft_frequencies > 0
    scale[mask] = 1 / rfft_frequencies[mask]**(alpha / 2)

    spectrum = white_rfft * scale
    noise = np.fft.irfft(spectrum, n=sample_number)

    noise = noise - np.mean(noise)
    noise = noise / np.std(noise)

    return noise

pink_noise = colored_noise(1)
brown_noise = colored_noise(2)

impulsive_noise = np.zeros(sample_number)
impulse_mask = rng.random(sample_number) < 0.01
impulsive_noise[impulse_mask] = rng.normal(0, 8, np.sum(impulse_mask))

white_frequencies, white_psd = welch(white_noise, fs, nperseg=1024)
pink_frequencies, pink_psd = welch(pink_noise, fs, nperseg=1024)
brown_frequencies, brown_psd = welch(brown_noise, fs, nperseg=1024)

def estimate_slope(frequencies, psd):
    mask = (frequencies >= 1) & (frequencies <= 200)

    log_frequencies = np.log10(frequencies[mask])
    log_psd = np.log10(psd[mask])

    slope = np.polyfit(log_frequencies, log_psd, 1)[0]

    return slope

white_slope = estimate_slope(white_frequencies, white_psd)
pink_slope = estimate_slope(pink_frequencies, pink_psd)
brown_slope = estimate_slope(brown_frequencies, brown_psd)

print("Samples:", sample_number)
print("White mean:", np.mean(white_noise))
print("White variance:", np.var(white_noise))
print("Number of impulses:", np.sum(impulse_mask))
print()
print("White PSD slope:", white_slope)
print("Pink PSD slope:", pink_slope)
print("Brown PSD slope:", brown_slope)

samples_to_show = int(fs)

fig, axes = plt.subplots(4, 1, figsize=(10, 9), sharex=True)

axes[0].plot(time[:samples_to_show], white_noise[:samples_to_show])
axes[0].set_title("White Noise")
axes[0].set_ylabel("Amplitude")
axes[0].grid(True)

axes[1].plot(time[:samples_to_show], pink_noise[:samples_to_show])
axes[1].set_title("Pink Noise - 1/f")
axes[1].set_ylabel("Amplitude")
axes[1].grid(True)

axes[2].plot(time[:samples_to_show], brown_noise[:samples_to_show])
axes[2].set_title("Brown Noise - 1/f²")
axes[2].set_ylabel("Amplitude")
axes[2].grid(True)

axes[3].plot(time[:samples_to_show], impulsive_noise[:samples_to_show])
axes[3].set_title("Impulsive Noise")
axes[3].set_xlabel("Time [s]")
axes[3].set_ylabel("Amplitude")
axes[3].grid(True)

plt.tight_layout()

plt.figure(figsize=(10, 6))

plt.loglog(white_frequencies[1:], white_psd[1:], label="White noise")
plt.loglog(pink_frequencies[1:], pink_psd[1:], label="Pink noise")
plt.loglog(brown_frequencies[1:], brown_psd[1:], label="Brown noise")

plt.title("Noise Power Spectral Density")
plt.xlabel("Frequency [Hz]")
plt.ylabel("PSD")
plt.grid(True)
plt.legend()
plt.tight_layout()

plt.show()
