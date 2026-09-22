import argparse
from scipy.io import wavfile
from scipy.signal import butter, sosfilt
import numpy as np
from pathlib import Path

parser = argparse.ArgumentParser(description="Filter a WAV audio file.")
parser.add_argument("input_path", help="Path of the input file.")
parser.add_argument("output_path", help="Path of the output file.")
parser.add_argument("--cutoff", type=float, default=1000.0, help="Cutoff frequency value.")
parser.add_argument("--order", type=int, default=4, help="Order of the filter.")
args = parser.parse_args()

output_path = Path(args.output_path)
if output_path.exists():
    parser.error("There is already a file on that path. Choose another one!")

sampling_frequency, audio_data = wavfile.read(args.input_path)
print("Sampling frequency:", sampling_frequency)
print("Data_type", audio_data.dtype)
print("Shape:", audio_data.shape)

if audio_data.dtype != np.int16:
    parser.error("Audio data must be of type int16.")
if args.order < 1:
    parser.error("Order cannot be less than 1.")
if not (0 < args.cutoff < sampling_frequency / 2):
    parser.error("Cutoff frequency must be between 0 and Nyquist frequency.")

input_signal = audio_data.astype(np.float64) / 32768.0
sos = butter(args.order, args.cutoff, btype="lowpass", fs=sampling_frequency, output="sos")
output_signal = sosfilt(sos, input_signal, axis=0)

scaled_output = np.rint(output_signal * 32768.0)
if np.any((scaled_output < -32768) | (scaled_output > 32767)):
    print("Warning: output exceeds the int16 range; clipping will be applied.")
output_data = (np.clip(scaled_output, -32768, 32767)).astype(np.int16)

wavfile.write(str(output_path), sampling_frequency, output_data)
print("Saved:", output_path)
