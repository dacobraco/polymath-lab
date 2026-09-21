from scipy.signal import butter, cheby1, freqz_sos
import numpy as np
import matplotlib.pyplot as plt

filter_order = 4
cutoff_frequency = 10.0
sampling_frequency = 200.0
passband_ripple_db = 1.0

butter_sos = butter(filter_order, cutoff_frequency, fs=sampling_frequency, output="sos")
cheby_sos = cheby1(filter_order, passband_ripple_db, cutoff_frequency, fs=sampling_frequency, output="sos")
butter_frequencies, butter_response = freqz_sos(butter_sos, worN=2048, fs=sampling_frequency)
cheby_frequencies, cheby_response = freqz_sos(cheby_sos, worN=2048, fs=sampling_frequency)

print("Butterworth:", butter_sos)
print("Chebyshev I:", cheby_sos)

check_frequencies = [2.0, 10.0, 15.0, 30.0]

_, butter_check = freqz_sos(butter_sos, worN=check_frequencies, fs=sampling_frequency)
_, cheby_check = freqz_sos(cheby_sos, worN=check_frequencies, fs=sampling_frequency)

print("Frequencies [Hz]:", check_frequencies)
print("Butterworth amplitude gains:", np.round(np.abs(butter_check), 6))
print("Chebyshev I amplitude gains:", np.round(np.abs(cheby_check), 6))

plt.figure(figsize=(10, 5))

plt.plot(butter_frequencies, np.abs(butter_response), label="Butterworth")
plt.plot(cheby_frequencies, np.abs(cheby_response), label="Chebyshev I")
plt.axvline(cutoff_frequency, color="gray", linestyle="--", label=f"Frequency boundary: {cutoff_frequency:g} Hz")

plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude gain")
plt.title("Fourth-Order Butterworth and Chebyshev I Filters")
plt.xlim(0, 40)
plt.ylim(0, 1.1)
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
