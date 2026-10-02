
import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)

fs = 100_000
fc = 5000
f0 = 3000
f1 = 5000
Tb = 0.001
noise_std = 0.65

bits = rng.integers(0, 2, 1000)
samples_per_bit = int(fs * Tb)

bit_stream = np.repeat(bits, samples_per_bit)
t = np.arange(len(bit_stream)) / fs

carrier = np.cos(2 * np.pi * fc * t)

ask_signal = bit_stream * carrier

frequencies = np.where(bit_stream == 1, f1, f0)
phase = np.concatenate(([0], np.cumsum(frequencies[:-1]))) * 2 * np.pi / fs
fsk_signal = np.cos(phase)

phases = np.where(bit_stream == 1, 0, np.pi)
psk_signal = np.cos(2 * np.pi * fc * t + phases)

noise = rng.normal(0, noise_std, len(ask_signal))
received_signal = ask_signal + noise

received_blocks = received_signal.reshape(-1, samples_per_bit)
bit_powers = np.mean(received_blocks**2, axis=1)

thresholds = [0.25, 0.45, 0.67, 0.85]

for threshold in thresholds:
    reconstructed = (bit_powers >= threshold).astype(int)
    errors = np.sum(bits != reconstructed)
    ber = errors / len(bits)

    print(f"Threshold: {threshold:.2f} | Errors: {errors} | BER: {ber:.2%}")

plt.figure(figsize=(11, 7))

plt.subplot(4, 1, 1)
plt.plot(t, ask_signal)
plt.ylabel("ASK")
plt.xlim(0, 0.008)
plt.grid(True)

plt.subplot(4, 1, 2)
plt.plot(t, fsk_signal)
plt.ylabel("FSK")
plt.xlim(0, 0.008)
plt.grid(True)

plt.subplot(4, 1, 3)
plt.plot(t, psk_signal)
plt.ylabel("BPSK")
plt.xlim(0, 0.008)
plt.grid(True)

plt.subplot(4, 1, 4)
plt.plot(t, received_signal)
plt.ylabel("Noisy ASK")
plt.xlabel("Time [s]")
plt.xlim(0, 0.008)
plt.grid(True)

plt.tight_layout()
plt.show()
