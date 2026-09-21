import numpy as np
from scipy.fft import rfft, rfftfreq, irfft

sampling_frequency = 44100
duration = 2.0
low_gain = 1.5
mid_gain = 0.5
high_gain = 1.0
time = np.arange(0, duration, 1 / sampling_frequency)

input_signal = 0.2 * np.sin(2*np.pi*100*time) + 0.2 * np.sin(2*np.pi*1000*time) + 0.2 * np.sin(2*np.pi*5000*time)
spectrum = rfft(input_signal)
frequencies = rfftfreq(len(input_signal), d=1/sampling_frequency)
equalized_spectrum = spectrum.copy()

low_mask = frequencies < 300
mid_mask = (frequencies >= 300) & (frequencies < 3000)
high_mask = frequencies >= 3000

equalized_spectrum[low_mask] *= low_gain
equalized_spectrum[mid_mask] *= mid_gain
equalized_spectrum[high_mask] *= high_gain

output_signal = irfft(equalized_spectrum, len(input_signal))

sample_count = len(input_signal)

input_amplitudes = 2 * np.abs(spectrum) / sample_count
output_amplitudes = 2 * np.abs(rfft(output_signal)) / sample_count

for target_frequency, expected_gain in [(100, low_gain), (1000, mid_gain), (5000, high_gain)]:
    index = np.argmin(np.abs(frequencies - target_frequency))
    amplitude_before = input_amplitudes[index]
    amplitude_after = output_amplitudes[index]
    measured_gain = amplitude_after / amplitude_before

    print(f"Frequency: {frequencies[index]:.1f} Hz")
    print(f"Amplitude before: {amplitude_before:.6f}")
    print(f"Amplitude after:  {amplitude_after:.6f}")
    print(f"Gain: {measured_gain:.6f}, expected: {expected_gain:.6f}")
