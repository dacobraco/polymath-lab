from pathlib import Path
import argparse

import numpy as np
import soundfile as sf


def load_wav(file_path):
    path = Path(file_path)

    if not path.is_file():
        raise FileNotFoundError(f"WAV file not found: {path}")

    loaded_signal, sample_rate = sf.read(path)
    original_shape = loaded_signal.shape

    if loaded_signal.ndim not in (1, 2):
        raise ValueError("WAV data must be mono or multichannel.")

    if not np.all(np.isfinite(loaded_signal)):
        raise ValueError("WAV data contains non-finite values.")

    if loaded_signal.ndim == 1:
        channel_count = 1
        mono_signal = loaded_signal
    else:
        channel_count = loaded_signal.shape[1]
        mono_signal = np.mean(loaded_signal, axis=1)

    if len(mono_signal) < 2:
        raise ValueError("WAV signal must contain at least two sample frames.")

    return mono_signal, sample_rate, channel_count, original_shape

def select_segment(signal, sample_rate, start_time, segment_duration):
    if sample_rate <= 0:
        raise ValueError("Sample rate must be positive.")
    if start_time < 0:
        raise ValueError("Start time must be non-negative.")
    if segment_duration <= 0:
        raise ValueError("Duration must be positive.")
    start_index = int(start_time * sample_rate)
    segment_frame_count = int(segment_duration * sample_rate)
    if segment_frame_count < 2:
        raise ValueError("The segment is too short.")
    end_index = start_index + segment_frame_count
    if start_index >= len(signal):
        raise ValueError("Start time is outside the signal.")
    if end_index > len(signal):
        raise ValueError("End time is outside the signal.")
    segment = signal[start_index:end_index]

    return segment, start_index, end_index

def calculate_amplitude_spectrum(signal, sample_rate, use_hann_window=True):
    if sample_rate <= 0:
        raise ValueError("Sample rate must be positive.")
    npsignal = np.asarray(signal, dtype=float)
    if npsignal.ndim != 1:
        raise ValueError("Signal must be one-dimensional.")
    if len(npsignal) < 2:
        raise ValueError("Signal must contain at least two samples.")
    if not np.all(np.isfinite(npsignal)):
        raise ValueError("Signal contains non-finite values.")
    avg = np.mean(npsignal)
    centered_signal = npsignal - avg
    sample_count = len(centered_signal)

    if use_hann_window:
        window = np.hanning(sample_count)
    else:
        window = np.ones(sample_count)

    window_sum = np.sum(window)

    if window_sum == 0:
        raise ValueError("Window sum must be positive.")

    windowed_signal = centered_signal * window

    complex_spectrum = np.fft.rfft(windowed_signal)
    frequencies = np.fft.rfftfreq(sample_count, d=1/sample_rate)
    amplitudes = np.abs(complex_spectrum) / window_sum
    if sample_count % 2 == 0:
        amplitudes[1:-1] *= 2
    else:
        amplitudes[1:] *= 2
    frequency_resolution = sample_rate / sample_count

    return frequencies, amplitudes, frequency_resolution, avg

def find_dominant_frequency(frequencies, amplitudes, min_frequency=20.0, max_frequency=None):
    frequencies = np.asarray(frequencies, dtype=float)
    amplitudes = np.asarray(amplitudes, dtype=float)

    if frequencies.ndim != 1 or amplitudes.ndim != 1:
        raise ValueError("Frequencies and amplitudes must be one-dimensional.")

    if len(frequencies) != len(amplitudes):
        raise ValueError("Frequencies and amplitudes must have equal lengths.")

    if len(frequencies) == 0:
        raise ValueError("Frequencies and amplitudes must not be empty.")

    if not np.all(np.isfinite(frequencies)):
        raise ValueError("Frequencies contain non-finite values.")

    if not np.all(np.isfinite(amplitudes)):
        raise ValueError("Amplitudes contain non-finite values.")

    if not np.isfinite(min_frequency) or min_frequency < 0:
        raise ValueError("Minimum frequency must be finite and non-negative.")

    if max_frequency is not None:
        if not np.isfinite(max_frequency):
            raise ValueError("Maximum frequency must be finite.")

        if max_frequency <= min_frequency:
            raise ValueError("Maximum frequency must be greater than minimum frequency.")

    frequency_mask = frequencies >= min_frequency

    if max_frequency is not None:
        frequency_mask &= frequencies <= max_frequency

    valid_indices = np.flatnonzero(frequency_mask)

    if len(valid_indices) == 0:
        raise ValueError("The selected frequency range contains no bins.")

    valid_amplitudes = amplitudes[valid_indices]
    local_dominant_index = np.argmax(valid_amplitudes)
    dominant_index = int(valid_indices[local_dominant_index])

    dominant_frequency = frequencies[dominant_index]
    dominant_amplitude = amplitudes[dominant_index]

    return dominant_frequency, dominant_amplitude, dominant_index

def parse_arguments():
    parser = argparse.ArgumentParser(description="Analyze the amplitude spectrum of a WAV file.")
    parser.add_argument("file_path", help="Path to the input WAV file.")
    parser.add_argument("--start", type=float, default=0.0, help="Segment start time in seconds.")
    parser.add_argument("--duration", type=float, required=True, help="Segment duration in seconds.")
    parser.add_argument("--min-frequency", type=float, default=20.0, help="Minimum frequency in Hz.")
    parser.add_argument("--max-frequency", type=float, default=None, help="Maximum frequency in Hz.")

    args = parser.parse_args()

    return args

def main():
    args = parse_arguments()
    signal, sample_rate, channel_count, original_shape = load_wav(args.file_path)
    segment, start_index, end_index = select_segment(signal, sample_rate, args.start, args.duration)
    frequencies, amplitudes, frequency_resolution, segment_mean = calculate_amplitude_spectrum(segment, sample_rate)
    dominant_frequency, dominant_amplitude, dominant_index = find_dominant_frequency(frequencies, amplitudes, args.min_frequency, args.max_frequency)
    print()
    print("FFT spectrum analysis")
    print("Input file:", args.file_path)
    print("Sample rate:", sample_rate)
    print("Original channels:", channel_count)
    print("Original shape:", original_shape)
    print("Requested start time:", args.start)
    print("Requested duration:", args.duration)
    print("Start index:", start_index)
    print("End index:", end_index)
    print("Segment frames:", len(segment))
    print("Actual segment duration:", len(segment) / sample_rate)
    print("Segment mean before centering:", segment_mean)
    print("Hann window used:", True)
    print("Frequency-bin count:", len(frequencies))
    print("Frequency resolution:", frequency_resolution)
    print("Minimum analysis frequency:", args.min_frequency)

    if args.max_frequency is None:
        print("Maximum analysis frequency:", frequencies[-1])
    else:
        print("Maximum analysis frequency:", args.max_frequency)

    print("Dominant frequency:", dominant_frequency)
    print("Dominant amplitude:", dominant_amplitude)
    print("Dominant bin:", dominant_index)


if __name__ == "__main__":
    main()
