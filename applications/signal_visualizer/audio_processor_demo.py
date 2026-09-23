import subprocess
import sys
from pathlib import Path

import numpy as np
from scipy.fft import rfft, rfftfreq

from audio_processor import read_mono_wav, write_mono_wav


if __name__ == "__main__":
    project_directory = Path(__file__).resolve().parent
    demo_directory = project_directory / "audio_processor_demo"
    demo_directory.mkdir(exist_ok=True)

    noisy_path = demo_directory / "noisy.wav"
    cleaned_path = demo_directory / "cleaned.wav"
    equalized_path = demo_directory / "equalized.wav"

    for output_path in [noisy_path, cleaned_path, equalized_path]:
        if output_path.exists():
            raise FileExistsError(f"Demo file already exists: {output_path}")

    sampling_frequency = 44100
    duration = 5.0
    time = np.arange(int(sampling_frequency * duration)) / sampling_frequency

    clean_signal = 0.2 * np.sin(2 * np.pi * 200 * time)
    clean_signal += 0.2 * np.sin(2 * np.pi * 1000 * time)
    clean_signal += 0.2 * np.sin(2 * np.pi * 4000 * time)
    noisy_signal = clean_signal + 0.15 * np.sin(2 * np.pi * 50 * time)

    input_factor = write_mono_wav(noisy_path, sampling_frequency, noisy_signal)
    assert input_factor == 1.0

    script_path = project_directory / "audio_processor.py"
    command = [sys.executable, str(script_path), str(noisy_path)]

    subprocess.run(command + [str(cleaned_path)], check=True)
    subprocess.run(command + [str(equalized_path), "--low-gain-db", "-6", "--mid-gain-db", "0", "--high-gain-db", "6"], check=True)

    signals = []

    for audio_path in [noisy_path, cleaned_path, equalized_path]:
        loaded_rate, loaded_signal = read_mono_wav(audio_path)
        assert loaded_rate == sampling_frequency
        assert len(loaded_signal) == len(time)
        signals.append(loaded_signal)

    start_index = 2 * sampling_frequency
    sample_count = len(signals[0]) - start_index
    frequencies = rfftfreq(sample_count, d=1 / sampling_frequency)

    spectra = [
        2 * np.abs(rfft(signal[start_index:])) / sample_count
        for signal in signals
    ]

    print()
    print("Amplitudes measured from 2.0 to 5.0 seconds:")
    print("Frequency [Hz] | Noisy        | Cleaned      | Equalized")

    for target_frequency in [50, 200, 1000, 4000]:
        index = np.argmin(np.abs(frequencies - target_frequency))
        before = spectra[0][index]
        cleaned = spectra[1][index]
        equalized = spectra[2][index]

        print(f"{target_frequency:14.1f} | {before:.8f}   | {cleaned:.8f}   | {equalized:.8f}")

        if target_frequency == 50:
            assert cleaned / before < 0.01
        else:
            assert abs(cleaned / before - 1.0) < 0.01

    print()
    print("Measured EQ gains relative to the cleaned audio:")

    for target_frequency, gain_db in [(200, -6.0), (1000, 0.0), (4000, 6.0)]:
        index = np.argmin(np.abs(frequencies - target_frequency))
        measured_gain = spectra[2][index] / spectra[1][index]
        expected_gain = 10 ** (gain_db / 20)

        print(f"{target_frequency:.1f} Hz: measured={measured_gain:.6f}, expected={expected_gain:.6f}")
        assert abs(measured_gain / expected_gain - 1.0) < 0.01

    print()
    print("Audio demo verification passed.")
    print("Demo directory:", demo_directory)
