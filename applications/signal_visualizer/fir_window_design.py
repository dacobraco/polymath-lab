import numpy as np
from scipy.signal import firwin


sample_rate = 200.0
number_of_taps = 51
window_name = "hamming"

lowpass_cutoff = 35.0
highpass_cutoff = 50.0
bandpass_cutoff = [50.0, 80.0]


lowpass_coefficients = firwin(number_of_taps, lowpass_cutoff, fs=sample_rate, window=window_name, pass_zero=True)

highpass_coefficients = firwin(number_of_taps, highpass_cutoff, fs=sample_rate, window=window_name, pass_zero=False)

bandpass_coefficients = firwin(number_of_taps, bandpass_cutoff, fs=sample_rate, window=window_name, pass_zero=False)


filter_order = number_of_taps - 1
delay_samples = (number_of_taps - 1) / 2
delay_seconds = delay_samples / sample_rate


def print_filter_summary(name, coefficients):
    middle_index = len(coefficients) // 2

    print()
    print(name)
    print("-" * len(name))
    print("Number of taps:", len(coefficients))
    print("Coefficient sum:", np.sum(coefficients))
    print("Symmetric:", np.allclose(coefficients, coefficients[::-1]))
    print("First coefficient:", coefficients[0])
    print("Middle coefficient:", coefficients[middle_index])
    print("Last coefficient:", coefficients[-1])


print("FIR window design")
print("=================")
print("Sample rate:", sample_rate, "Hz")
print("Nyquist frequency:", sample_rate / 2, "Hz")
print("Window:", window_name)
print("Filter order:", filter_order)
print("Linear-phase delay:", delay_samples, "samples")
print("Linear-phase delay:", delay_seconds, "seconds")

print_filter_summary("Low-pass filter", lowpass_coefficients)
print_filter_summary("High-pass filter", highpass_coefficients)
print_filter_summary("Band-pass filter", bandpass_coefficients)


assert len(lowpass_coefficients) == number_of_taps
assert len(highpass_coefficients) == number_of_taps
assert len(bandpass_coefficients) == number_of_taps

assert np.allclose(lowpass_coefficients, lowpass_coefficients[::-1])
assert np.allclose(highpass_coefficients, highpass_coefficients[::-1])
assert np.allclose(bandpass_coefficients, bandpass_coefficients[::-1])

assert np.isclose(np.sum(lowpass_coefficients), 1.0)
assert abs(np.sum(highpass_coefficients)) < 0.01
assert abs(np.sum(bandpass_coefficients)) < 0.01

print()
print("All FIR design checks passed.")
