import numpy as np
import argparse
from scipy.io import wavfile
from scipy.fft import rfft, rfftfreq, irfft
from scipy.signal import iirnotch, tf2sos, sosfilt
from pathlib import Path

def equalize_audio(input_signal, sampling_frequency, low_gain_db, mid_gain_db, high_gain_db):
    low_gain = 10 ** (low_gain_db / 20)
    mid_gain = 10 ** (mid_gain_db / 20)
    high_gain = 10 ** (high_gain_db / 20)
    spectrum = rfft(input_signal)
    frequencies = rfftfreq(len(input_signal), d=1/sampling_frequency)
    equalized_spectrum = spectrum.copy()

    low_mask = frequencies < 300
    mid_mask = (frequencies >= 300) & (frequencies < 3000)
    high_mask = frequencies >= 3000

    equalized_spectrum[low_mask] *= low_gain
    equalized_spectrum[mid_mask] *= mid_gain
    equalized_spectrum[high_mask] *= high_gain

    output = irfft(equalized_spectrum, len(input_signal))
    return output

def remove_tonal_noise(input_signal, sampling_frequency, noise_frequency, quality_factor=30.0):
    b, a = iirnotch(noise_frequency, quality_factor, sampling_frequency)
    sos = tf2sos(b, a)
    filtered_signal = sosfilt(sos, input_signal)

    return filtered_signal

def read_mono_wav(input_path):
    sample_rate, audio_data = wavfile.read(input_path)
    if audio_data.dtype != "int16":
        raise ValueError("Audio data is not of type int16.")
    if audio_data.ndim != 1:
        raise ValueError("Audio data is not mono.")
    if len(audio_data) == 0:
        raise ValueError("Input signal must exist.")
    input_signal = audio_data.astype(np.float64) / 32768.0

    return sample_rate, input_signal

def write_mono_wav(output_path, sampling_frequency, output_signal):
    out_path = Path(output_path)
    if out_path.exists():
        raise FileExistsError("There is a file in the provided path.")
    if output_signal.ndim != 1:
        raise ValueError("Output signal is not mono.")
    if len(output_signal) == 0:
        raise ValueError("Output signal cannot be empty.")
    if not np.all(np.isfinite(output_signal)):
        raise ValueError("Output signal must contain only finite values.")
    max_amplitude = np.max(np.abs(output_signal))
    factor = 1.0
    if max_amplitude > 0.99:
        factor = 0.99 / max_amplitude
    scaled_signal = (np.rint((factor * output_signal) * 32768.0)).astype(np.int16)
    wavfile.write(out_path, sampling_frequency, scaled_signal)

    return factor

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", help="Path of the input file.")
    parser.add_argument("output_path", help="Path of the output file.")
    parser.add_argument("--noise-frequency", type=float, default=50.0, help="Noise frequency [Hz]")
    parser.add_argument("--quality-factor", type=float, default=30.0, help="Quality factor of the notch filter.")
    parser.add_argument("--low-gain-db", type=float, default=0.0, help="Low-band gain [dB].")
    parser.add_argument("--mid-gain-db", type=float, default=0.0, help="Mid-band gain [dB].")
    parser.add_argument("--high-gain-db", type=float, default=0.0, help="High-band gain [dB].")
    args = parser.parse_args()

    try:
        sampling_frequency, input_signal = read_mono_wav(args.input_path)

        if not np.isfinite(args.noise_frequency) or not (0.0 < args.noise_frequency < sampling_frequency / 2.0):
            parser.error("Incorrect noise frequency provided.")

        if not np.isfinite(args.quality_factor) or not (args.quality_factor > 0.0):
            parser.error("Incorrect quality factor provided.")

        if not (np.isfinite(args.low_gain_db) and np.isfinite(args.mid_gain_db) and np.isfinite(args.high_gain_db)) or not (-24 <= args.low_gain_db <= 24 and -24 <= args.mid_gain_db <= 24 and -24 <= args.high_gain_db <= 24):
            parser.error("Incorrect gains provided.")

        filtered_signal = remove_tonal_noise(input_signal, sampling_frequency, args.noise_frequency, args.quality_factor)
        equalized_signal = equalize_audio(filtered_signal, sampling_frequency, args.low_gain_db, args.mid_gain_db, args.high_gain_db)
        factor = write_mono_wav(args.output_path, sampling_frequency, equalized_signal)

    except (ValueError, OSError) as error:
        parser.error(str(error))

    print("Sampling frequency:", sampling_frequency)
    print("Number of samples:", len(input_signal))
    print("Scaling factor:", factor)
    print("Output path:", args.output_path)

if __name__ == "__main__":
    main()
