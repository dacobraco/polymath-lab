from scipy.signal import firwin, freqz, group_delay
import matplotlib.pyplot as plt
import numpy as np

sample_rate = 200.0
number_of_taps = 51
cutoff_frequency = 35.0

test_frequencies = [10.0, 20.0, 35.0, 50.0, 80.0]

passband_edge = 20.0
stopband_edge = 50.0

lowpass_coefficients = firwin(number_of_taps, cutoff_frequency, fs=sample_rate)

frequencies, response = freqz(lowpass_coefficients, worN=1024, fs=sample_rate)

magnitude = np.abs(response)
magnitude_db = 20 * np.log10(magnitude)

phase = np.angle(response)
unwrapped_phase = np.unwrap(phase)

passband_mask = frequencies <= passband_edge
stopband_mask = frequencies >= stopband_edge

best_passband_db = np.max(magnitude_db[passband_mask])
worst_passband_db = np.min(magnitude_db[passband_mask])

passband_ripple_db = best_passband_db - worst_passband_db

worst_stopband_db = np.max(magnitude_db[stopband_mask])

delay_frequencies, delay_samples = group_delay((lowpass_coefficients, [1.0]), w=1024, fs=sample_rate)

expected_delay_samples = (number_of_taps - 1) / 2
expected_delay_seconds = expected_delay_samples / sample_rate

for target_frequency in test_frequencies:
    nearest_index = np.argmin(np.abs(frequencies - target_frequency))

    print(
        "Target:", target_frequency,
        "\tActual:", frequencies[nearest_index],
        "\tMagnitude:", magnitude[nearest_index],
        "\tMagnitude in dB:", magnitude_db[nearest_index],
        "\nPhase:", phase[nearest_index],
        "\tUnwrapped phase:", unwrapped_phase[nearest_index]
    )

print()
print("Best passband magnitude:", best_passband_db, "dB")
print("Worst passband magnitude:", worst_passband_db, "dB")
print("Passband ripple:", passband_ripple_db, "dB")
print("Worst stopband magnitude:", worst_stopband_db, "dB")

print()
print("Number of group-delay points:", len(delay_samples))
print("First group delay:", delay_samples[0])
print("Minimum group delay:", np.min(delay_samples))
print("Maximum group delay:", np.max(delay_samples))
print("Expected group delay:", expected_delay_samples, "samples")
print("Expected group delay:", expected_delay_seconds, "seconds")

assert worst_passband_db >= -1.0
assert worst_stopband_db <= -40.0
assert np.allclose(delay_samples, expected_delay_samples, atol=1e-5)

print()
print("FIR frequency-response checks: PASSED")

plt.figure(figsize=(10, 6))

plt.plot(frequencies, magnitude_db)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude [dB]")
plt.title("FIR Low-Pass Frequency Response")

plt.grid(True)
plt.xlim(0, sample_rate / 2)
plt.ylim(-100, 5)

plt.tight_layout()


plt.figure(figsize=(10, 6))

plt.plot(frequencies, unwrapped_phase)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Phase [rad]")
plt.title("FIR Low-Pass Phase Response")

plt.grid(True)
plt.xlim(0, sample_rate / 2)

plt.tight_layout()


plt.figure(figsize=(10, 6))

plt.plot(delay_frequencies, delay_samples)

plt.xlabel("Frequency [Hz]")
plt.ylabel("Group Delay [samples]")
plt.title("FIR Low-Pass Group Delay")

plt.grid(True)
plt.xlim(0, sample_rate / 2)
plt.ylim(24.5, 25.5)

plt.tight_layout()
plt.show()
