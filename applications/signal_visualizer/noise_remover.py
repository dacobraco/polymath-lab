import numpy as np
from scipy.signal import butter, sosfilt

sampling_frequency = 44100.00
duration = 2.0
N = 4
Wn = 1000
time = np.arange(int(sampling_frequency * duration)) / sampling_frequency

clean_signal = 0.5 * np.sin(2*np.pi*440*time)
noise = 0.2 * np.sin(2*np.pi*6000*time)
noisy_signal = clean_signal + noise

sos = butter(N, Wn, fs=sampling_frequency, btype="lowpass", output="sos")
filtered_signal = sosfilt(sos, noisy_signal)

start_index = int(0.1 * sampling_frequency)

before = noisy_signal[start_index:]
after = filtered_signal[start_index:]

sample_count = len(before)
frequencies = np.fft.rfftfreq(sample_count, d=1 / sampling_frequency)

before_amplitudes = 2 * np.abs(np.fft.rfft(before)) / sample_count
after_amplitudes = 2 * np.abs(np.fft.rfft(after)) / sample_count

for target_frequency in [440, 6000]:
    index = np.argmin(np.abs(frequencies - target_frequency))
    amplitude_before = before_amplitudes[index]
    amplitude_after = after_amplitudes[index]

    print(f"Frequency: {frequencies[index]:.1f} Hz")
    print(f"Amplitude before: {amplitude_before:.8f}")
    print(f"Amplitude after:  {amplitude_after:.8f}")
