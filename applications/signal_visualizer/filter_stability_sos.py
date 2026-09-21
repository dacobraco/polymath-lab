from scipy.signal import butter, sosfilt, sos2zpk, lfilter
import numpy as np

filter_order = 4
cutoff_frequency = 10.0
sampling_frequency = 200.0

butter_sos = butter(filter_order, cutoff_frequency, fs=sampling_frequency, output="sos")
print("SOS coefficients:", butter_sos)
print("SOS shape:", butter_sos.shape)
print("First section:", butter_sos[0])

impulse = np.zeros(1000)
impulse[0] = 1.0
impulse_response = sosfilt(butter_sos, impulse)

print(impulse_response[:8])
print(impulse_response[-5:])

zeros, poles, gain = sos2zpk(butter_sos)
pole_magnitudes = np.abs(poles)
max_pole_magnitude = np.max(pole_magnitudes)

print("Poles:", poles)
print("Pole magnitudes:", pole_magnitudes)
print("Max pole magnitude:", max_pole_magnitude)
print("Stable:", max_pole_magnitude < 1.0)

comparison_order = 8

comparison_b, comparison_a = butter(comparison_order, cutoff_frequency, fs=sampling_frequency, output="ba")
comparison_sos = butter(comparison_order, cutoff_frequency, fs=sampling_frequency, output="sos")

reference_response = sosfilt(comparison_sos, impulse)

impulse_float32 = impulse.astype(np.float32)
b_float32 = comparison_b.astype(np.float32)
a_float32 = comparison_a.astype(np.float32)
sos_float32 = comparison_sos.astype(np.float32)

ba_response = lfilter(b_float32, a_float32, impulse_float32)
sos_response = sosfilt(sos_float32, impulse_float32)

ba_max_error = np.max(np.abs(ba_response - reference_response))
sos_max_error = np.max(np.abs(sos_response - reference_response))

print("BA float32 maximum absolute error:", ba_max_error)
print("SOS float32 maximum absolute error:", sos_max_error)
