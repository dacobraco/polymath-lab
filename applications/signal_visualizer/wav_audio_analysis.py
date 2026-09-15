import numpy as np
import soundfile as sf
from scipy.signal import find_peaks
import matplotlib.pyplot as plt

sample_rate = 44100
duration = 3.0
sample_count = int(sample_rate * duration)

times = np.arange(sample_count) / sample_rate

fundamental_frequency = 220.0
second_harmonic_frequency = 440.0
third_harmonic_frequency = 660.0

left_channel = (
    0.55 * np.sin(2 * np.pi * fundamental_frequency * times)
    + 0.20 * np.sin(2 * np.pi * second_harmonic_frequency * times)
    + 0.10 * np.sin(2 * np.pi * third_harmonic_frequency * times)
)

right_channel = (
    0.45 * np.sin(2 * np.pi * fundamental_frequency * times)
    + 0.25 * np.sin(2 * np.pi * second_harmonic_frequency * times)
    + 0.10 * np.sin(2 * np.pi * third_harmonic_frequency * times)
)

stereo_signal = np.column_stack((left_channel, right_channel))

output_path = "controlled_tone.wav"
sf.write(output_path, stereo_signal, sample_rate, subtype="PCM_16")

print("WAV written:", output_path)
print("Sample rate:", sample_rate)
print("Duration:", duration)
print("Sample frames:", sample_count)
print("Array shape:", stereo_signal.shape)
print("Largest absolute amplitude:", np.max(np.abs(stereo_signal)))

loaded_signal, loaded_sample_rate = sf.read(output_path)

loaded_frame_count = loaded_signal.shape[0]

if loaded_signal.ndim == 1:
    loaded_channel_count = 1
else:
    loaded_channel_count = loaded_signal.shape[1]

loaded_duration = loaded_frame_count / loaded_sample_rate
largest_loaded_amplitude = np.max(np.abs(loaded_signal))
maximum_write_read_error = np.max(np.abs(loaded_signal - stereo_signal))

print()
print("Loaded WAV information")
print("Loaded sample rate:", loaded_sample_rate)
print("Loaded sample frames:", loaded_frame_count)
print("Loaded channels:", loaded_channel_count)
print("Loaded array shape:", loaded_signal.shape)
print("Loaded data type:", loaded_signal.dtype)
print("Calculated duration:", loaded_duration)
print("Largest loaded amplitude:", largest_loaded_amplitude)
print("Maximum write-read error:", maximum_write_read_error)

left_channel_loaded = loaded_signal[:, 0]
right_channel_loaded = loaded_signal[:, 1]

mono_signal = (left_channel_loaded + right_channel_loaded) / 2

inspection_index = 100
expected_mono_value = (left_channel_loaded[inspection_index] + right_channel_loaded[inspection_index]) / 2
downmix_error = abs(mono_signal[inspection_index] - expected_mono_value)

print()
print("Stereo to mono downmix")
print("Left channel shape:", left_channel_loaded.shape)
print("Right channel shape:", right_channel_loaded.shape)
print("Mono signal shape:", mono_signal.shape)
print("Inspected frame:", inspection_index)
print("Left value:", left_channel_loaded[inspection_index])
print("Right value:", right_channel_loaded[inspection_index])
print("Calculated mono value:", mono_signal[inspection_index])
print("Downmix verification error:", downmix_error)
print("Largest mono amplitude:", np.max(np.abs(mono_signal)))

mono_mean = np.mean(mono_signal)
centered_mono_signal = mono_signal - mono_mean

window = np.hanning(loaded_frame_count)
windowed_signal = centered_mono_signal * window

spectrum = np.fft.rfft(windowed_signal)
frequencies = np.fft.rfftfreq(loaded_frame_count, d=1 / loaded_sample_rate)
amplitudes = 2 * np.abs(spectrum) / np.sum(window)

frequency_resolution = loaded_sample_rate / loaded_frame_count

print()
print("Frequency-domain analysis")
print("Mono mean before centering:", mono_mean)
print("Mean after centering:", np.mean(centered_mono_signal))
print("Frequency resolution:", frequency_resolution)
print("Number of rFFT bins:", len(frequencies))
print("First frequency:", frequencies[0])
print("Last frequency:", frequencies[-1])

target_frequencies = [220, 440, 660]

for target_frequency in target_frequencies:
    closest_bin_index = np.argmin(np.abs(frequencies - target_frequency))
    detected_frequency = frequencies[closest_bin_index]
    detected_amplitude = amplitudes[closest_bin_index]
    print(f"Target {target_frequency} Hz -> bin {closest_bin_index}, detected {detected_frequency} Hz, amplitude {detected_amplitude}")

minimum_peak_height = 0.02
minimum_peak_distance_hz = 50.0
minimum_peak_distance_bins = int(minimum_peak_distance_hz / frequency_resolution)

peak_indices, peak_properties = find_peaks(amplitudes, height=minimum_peak_height, distance=minimum_peak_distance_bins,)

peak_order = np.argsort(amplitudes[peak_indices])[::-1]
sorted_peak_indices = peak_indices[peak_order]

print()
print("Automatically detected spectral peaks")
print("Minimum peak height:", minimum_peak_height)
print("Minimum peak distance in Hz:", minimum_peak_distance_hz)
print("Minimum peak distance in bins:", minimum_peak_distance_bins)
print("Detected peak count:", len(sorted_peak_indices))

for peak_number, peak_index in enumerate(sorted_peak_indices, start=1):
    peak_frequency = frequencies[peak_index]
    peak_amplitude = amplitudes[peak_index]
    print(f"Peak {peak_number}: frequency {peak_frequency} Hz, amplitude {peak_amplitude}")

time_axis = np.arange(loaded_frame_count) / loaded_sample_rate

display_duration = 0.03
display_sample_count = int(display_duration * loaded_sample_rate)

frequency_limit = 1000.0
frequency_mask = frequencies <= frequency_limit

figure, axes = plt.subplots(2, 1, figsize=(10, 8))

axes[0].plot(time_axis[:display_sample_count], mono_signal[:display_sample_count])
axes[0].set_title("Mono waveform — first 30 ms")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Amplitude")
axes[0].grid(True)

axes[1].plot(frequencies[frequency_mask], amplitudes[frequency_mask])

for peak_index in sorted_peak_indices:
    peak_frequency = frequencies[peak_index]
    peak_amplitude = amplitudes[peak_index]

    if peak_frequency <= frequency_limit:
        axes[1].plot(peak_frequency, peak_amplitude, "ro")
        axes[1].annotate(
            f"{peak_frequency:.0f} Hz",
            (peak_frequency, peak_amplitude),
            textcoords="offset points",
            xytext=(0, 8),
            ha="center",
        )

axes[1].set_title("Mono amplitude spectrum")
axes[1].set_xlabel("Frequency [Hz]")
axes[1].set_ylabel("Amplitude")
axes[1].set_xlim(0, frequency_limit)
axes[1].grid(True)

figure.tight_layout()

figure_output_path = "controlled_tone_analysis.png"
figure.savefig(figure_output_path, dpi=150)

print()
print("Analysis figure saved:", figure_output_path)

plt.show()
