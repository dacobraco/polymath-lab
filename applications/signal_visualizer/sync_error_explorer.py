
import numpy as np
import matplotlib.pyplot as plt

number_of_symbols = 500
phase_deg = 60
symbol_rate = 100
frequency_offset = 1

rng = np.random.default_rng(42)
bits = rng.integers(0, 2, size=(number_of_symbols, 2))

pilot1 = 0
pilot2 = 10
bits[pilot1] = [1, 1]
bits[pilot2] = [1, 1]

n = np.arange(number_of_symbols)
time = n / symbol_rate
phase = np.deg2rad(phase_deg)

QPSK_symbols = []

for b0, b1 in bits:
    s = ((2*b0 - 1) + 1j * (2*b1 - 1)) / np.sqrt(2)
    QPSK_symbols.append(s)

QPSK_symbols = np.array(QPSK_symbols)

def calculate_ber(symbols, original_bits):
    received_I = np.where(symbols.real > 0, 1, 0)
    received_Q = np.where(symbols.imag > 0, 1, 0)
    received_bits = np.column_stack((received_I, received_Q))
    errors = np.sum(original_bits != received_bits)
    return errors / original_bits.size

rotated_symbols = QPSK_symbols * np.exp(1j * phase)
estimated_phase = np.angle(rotated_symbols[0] / QPSK_symbols[0])
auto_corrected_symbols = rotated_symbols * np.exp(-1j * estimated_phase)

phase_ber = calculate_ber(rotated_symbols, bits)
corrected_phase_ber = calculate_ber(auto_corrected_symbols, bits)

phase_over_time = 2 * np.pi * frequency_offset * time
frequency_rotated_symbols = QPSK_symbols * np.exp(1j * phase_over_time)
frequency_ber = calculate_ber(frequency_rotated_symbols, bits)

estimated_phase1 = np.angle(frequency_rotated_symbols[pilot1] / QPSK_symbols[pilot1])
estimated_phase2 = np.angle(frequency_rotated_symbols[pilot2] / QPSK_symbols[pilot2])

phase_difference = np.angle(np.exp(1j * (estimated_phase2 - estimated_phase1)))
delta_t = time[pilot2] - time[pilot1]
estimated_frequency_offset = phase_difference / (2 * np.pi * delta_t)

estimated_phase_over_time = estimated_phase1 + 2 * np.pi * estimated_frequency_offset * time
frequency_corrected_symbols = frequency_rotated_symbols * np.exp(-1j * estimated_phase_over_time)
corrected_frequency_ber = calculate_ber(frequency_corrected_symbols, bits)

print("Estimated phase:", np.rad2deg(estimated_phase))
print("Phase offset BER:", phase_ber)
print("Corrected phase BER:", corrected_phase_ber)
print("Actual frequency offset:", frequency_offset, "Hz")
print("Estimated frequency offset:", estimated_frequency_offset, "Hz")
print("Frequency offset BER:", frequency_ber)
print("Corrected frequency BER:", corrected_frequency_ber)

plt.figure(figsize=(7, 7))
plt.scatter(frequency_rotated_symbols.real, frequency_rotated_symbols.imag, label="Frequency Offset", s=15)
plt.scatter(QPSK_symbols.real, QPSK_symbols.imag, label="Original", s=60)
plt.title("QPSK - Frequency Offset")
plt.xlabel("Real (I)")
plt.ylabel("Imaginary (Q)")
plt.axhline(0)
plt.axvline(0)
plt.axis("equal")
plt.grid(True)
plt.legend()

plt.figure(figsize=(7, 7))
plt.scatter(frequency_corrected_symbols.real, frequency_corrected_symbols.imag, label="Corrected", s=25)
plt.scatter(QPSK_symbols.real, QPSK_symbols.imag, label="Original", s=60, alpha=0.5)
plt.title("QPSK - Automatic Frequency Correction")
plt.xlabel("Real (I)")
plt.ylabel("Imaginary (Q)")
plt.axhline(0)
plt.axvline(0)
plt.axis("equal")
plt.grid(True)
plt.legend()

samples_per_symbol = 16
rolloff = 0.35
span = 8

pulse_time = np.arange(-span * samples_per_symbol, span * samples_per_symbol + 1) / samples_per_symbol
pulse = np.sinc(pulse_time) * np.cos(np.pi * rolloff * pulse_time) / (1 - (2 * rolloff * pulse_time)**2)

upsampled = np.zeros(number_of_symbols * samples_per_symbol, dtype=complex)
upsampled[::samples_per_symbol] = QPSK_symbols

shaped_signal = np.convolve(upsampled, pulse, mode="full")
sampling_indices = np.arange(number_of_symbols) * samples_per_symbol + span * samples_per_symbol

timing_offsets = [0, 2, 4, 6, 8, 10, 12]
timing_ber = []

for offset in timing_offsets:
    sampled_symbols = shaped_signal[sampling_indices + offset]
    current_ber = calculate_ber(sampled_symbols, bits)
    timing_ber.append(current_ber)
    print(f"Offset: {offset / samples_per_symbol:.3f}T, BER: {current_ber:.3f}")

plt.figure(figsize=(8, 5))
plt.plot(np.array(timing_offsets) / samples_per_symbol, timing_ber, marker="o")
plt.xlabel("Timing Offset / Symbol Duration")
plt.ylabel("BER")
plt.title("QPSK - Timing Synchronization Error")
plt.grid(True)
plt.show()
