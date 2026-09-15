import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy.signal import find_peaks

input_path = "recorded_voice.wav"

loaded_signal, sample_rate = sf.read(input_path)

original_shape = loaded_signal.shape

if loaded_signal.ndim == 1:
    mono_signal = loaded_signal
else:
    mono_signal = np.mean(loaded_signal, axis=1)

frame_count = len(mono_signal)
duration = frame_count / sample_rate
time_axis = np.arange(frame_count) / sample_rate

mean_amplitude = np.mean(mono_signal)
largest_amplitude = np.max(np.abs(mono_signal))

print("Real voice WAV information")
print("Input path:", input_path)
print("Sample rate:", sample_rate)
print("Original array shape:", original_shape)
print("Mono array shape:", mono_signal.shape)
print("Sample frames:", frame_count)
print("Calculated duration:", duration)
print("Mean amplitude:", mean_amplitude)
print("Largest absolute amplitude:", largest_amplitude)

figure, axis = plt.subplots(figsize=(10, 4))

axis.plot(time_axis, mono_signal)
axis.set_title("Recorded voice waveform")
axis.set_xlabel("Time [s]")
axis.set_ylabel("Amplitude")
axis.set_xlim(0, duration)
axis.grid(True)

figure.tight_layout()

figure_output_path = "recorded_voice_waveform.png"
figure.savefig(figure_output_path, dpi=150)

print("Waveform figure saved:", figure_output_path)

plt.show()

segment_start_time = 1.0
segment_end_time = 2.0

segment_start_index = int(segment_start_time * sample_rate)
segment_end_index = int(segment_end_time * sample_rate)

analysis_segment = mono_signal[segment_start_index:segment_end_index]
segment_mean = np.mean(analysis_segment)
centered_segment = analysis_segment - segment_mean

segment_frame_count = len(centered_segment)
segment_duration = segment_frame_count / sample_rate
frequency_resolution = sample_rate / segment_frame_count

window = np.hanning(segment_frame_count)
windowed_segment = centered_segment * window

spectrum = np.fft.rfft(windowed_segment)
frequencies = np.fft.rfftfreq(segment_frame_count, d=1 / sample_rate)
amplitudes = 2 * np.abs(spectrum) / np.sum(window)

print()
print("Selected voice segment")
print("Start time:", segment_start_time)
print("End time:", segment_end_time)
print("Start index:", segment_start_index)
print("End index:", segment_end_index)
print("Segment frames:", segment_frame_count)
print("Segment duration:", segment_duration)
print("Segment mean before centering:", segment_mean)
print("Segment mean after centering:", np.mean(centered_segment))
print("Frequency resolution:", frequency_resolution)

display_duration = 0.03
display_frame_count = int(display_duration * sample_rate)
segment_time_axis = np.arange(segment_frame_count) / sample_rate

frequency_limit = 2000.0
frequency_mask = frequencies <= frequency_limit

figure, axes = plt.subplots(2, 1, figsize=(10, 8))

axes[0].plot(segment_time_axis[:display_frame_count], centered_segment[:display_frame_count])
axes[0].set_title("Recorded voice — 30 ms from selected segment")
axes[0].set_xlabel("Time inside segment [s]")
axes[0].set_ylabel("Amplitude")
axes[0].grid(True)

axes[1].plot(frequencies[frequency_mask], amplitudes[frequency_mask])
axes[1].set_title("Recorded voice amplitude spectrum")
axes[1].set_xlabel("Frequency [Hz]")
axes[1].set_ylabel("Amplitude")
axes[1].set_xlim(0, frequency_limit)
axes[1].grid(True)

figure.tight_layout()

spectrum_figure_path = "recorded_voice_spectrum.png"
figure.savefig(spectrum_figure_path, dpi=150)

print("Spectrum figure saved:", spectrum_figure_path)

plt.show()

minimum_analysis_frequency = 60.0
maximum_analysis_frequency = 1200.0

analysis_band_mask = ((frequencies >= minimum_analysis_frequency) & (frequencies <= maximum_analysis_frequency))

band_frequencies = frequencies[analysis_band_mask]
band_amplitudes = amplitudes[analysis_band_mask]

largest_band_amplitude = np.max(band_amplitudes)
minimum_peak_prominence = 0.02 * largest_band_amplitude

minimum_peak_distance_hz = 50.0
minimum_peak_distance_bins = int(minimum_peak_distance_hz / frequency_resolution)

peak_indices, peak_properties = find_peaks(
    band_amplitudes,
    prominence=minimum_peak_prominence,
    distance=minimum_peak_distance_bins,
)

detected_peak_frequencies = band_frequencies[peak_indices]
detected_peak_amplitudes = band_amplitudes[peak_indices]
detected_peak_prominences = peak_properties["prominences"]

print()
print("Automatically detected voice peaks")
print("Analysis range:", minimum_analysis_frequency, "to", maximum_analysis_frequency, "Hz")
print("Largest band amplitude:", largest_band_amplitude)
print("Minimum prominence:", minimum_peak_prominence)
print("Minimum peak distance:", minimum_peak_distance_hz, "Hz")
print("Detected peak count:", len(detected_peak_frequencies))

for peak_number in range(len(detected_peak_frequencies)):
    peak_frequency = detected_peak_frequencies[peak_number]
    peak_amplitude = detected_peak_amplitudes[peak_number]
    peak_prominence = detected_peak_prominences[peak_number]
    print(f"Peak {peak_number + 1}: frequency {peak_frequency} Hz, amplitude {peak_amplitude}, prominence {peak_prominence}")

if len(detected_peak_frequencies) > 1:
    peak_spacings = np.diff(detected_peak_frequencies)
    print("Spacings between neighboring detected peaks:", peak_spacings)
