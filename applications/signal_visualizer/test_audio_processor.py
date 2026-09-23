import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
from scipy.fft import rfft, rfftfreq
from scipy.io import wavfile

from audio_processor import equalize_audio, remove_tonal_noise, read_mono_wav, write_mono_wav


def test_neutral_equalizer_preserves_odd_length_signal():
    sampling_frequency = 44100
    time = np.arange(44101) / sampling_frequency
    input_signal = 0.2 * np.sin(2 * np.pi * 200 * time)
    original_signal = input_signal.copy()

    output_signal = equalize_audio(input_signal, sampling_frequency, 0.0, 0.0, 0.0)

    assert output_signal.shape == input_signal.shape
    assert np.array_equal(input_signal, original_signal)
    assert np.max(np.abs(output_signal - input_signal)) < 1e-12


def test_equalizer_applies_requested_band_gains():
    sampling_frequency = 44100
    time = np.arange(sampling_frequency) / sampling_frequency

    low_tone = 0.2 * np.sin(2 * np.pi * 200 * time)
    mid_tone = 0.2 * np.sin(2 * np.pi * 1000 * time)
    high_tone = 0.2 * np.sin(2 * np.pi * 4000 * time)
    input_signal = low_tone + mid_tone + high_tone

    output_signal = equalize_audio(input_signal, sampling_frequency, -6.0, 0.0, 6.0)
    expected_signal = low_tone * 10 ** (-6.0 / 20) + mid_tone + high_tone * 10 ** (6.0 / 20)

    assert np.max(np.abs(output_signal - expected_signal)) < 1e-12


def test_notch_suppresses_noise_and_preserves_useful_tones():
    sampling_frequency = 44100
    time = np.arange(5 * sampling_frequency) / sampling_frequency

    clean_signal = 0.2 * np.sin(2 * np.pi * 200 * time)
    clean_signal += 0.2 * np.sin(2 * np.pi * 1000 * time)
    clean_signal += 0.2 * np.sin(2 * np.pi * 4000 * time)
    noisy_signal = clean_signal + 0.15 * np.sin(2 * np.pi * 50 * time)
    original_signal = noisy_signal.copy()

    filtered_signal = remove_tonal_noise(noisy_signal, sampling_frequency, 50.0, 30.0)

    assert filtered_signal.shape == noisy_signal.shape
    assert np.array_equal(noisy_signal, original_signal)
    assert np.all(np.isfinite(filtered_signal))

    before = noisy_signal[2 * sampling_frequency:]
    after = filtered_signal[2 * sampling_frequency:]
    frequencies = rfftfreq(len(before), d=1 / sampling_frequency)
    before_spectrum = np.abs(rfft(before))
    after_spectrum = np.abs(rfft(after))

    for target_frequency in [50, 200, 1000, 4000]:
        index = np.argmin(np.abs(frequencies - target_frequency))
        measured_gain = after_spectrum[index] / before_spectrum[index]

        if target_frequency == 50:
            assert measured_gain < 0.01
        else:
            assert abs(measured_gain - 1.0) < 0.01


@pytest.mark.parametrize("samples, expected_factor", [
    ([0.0, 0.0, 0.0], 1.0),
    ([-0.2, 0.0, 0.2], 1.0),
    ([-0.995, 0.0, 0.5], 0.99 / 0.995),
    ([-1.5, 0.0, 0.3], 0.99 / 1.5),
])
def test_wav_round_trip(tmp_path, samples, expected_factor):
    sampling_frequency = 44100
    input_signal = np.array(samples, dtype=np.float64)
    original_signal = input_signal.copy()
    output_path = tmp_path / "round_trip.wav"

    factor = write_mono_wav(output_path, sampling_frequency, input_signal)
    loaded_rate, loaded_signal = read_mono_wav(output_path)

    expected_signal = original_signal * expected_factor
    max_error = np.max(np.abs(loaded_signal - expected_signal))

    assert loaded_rate == sampling_frequency
    assert loaded_signal.shape == input_signal.shape
    assert np.array_equal(input_signal, original_signal)
    assert abs(factor - expected_factor) < 1e-12
    assert max_error <= 0.5 / 32768.0 + 1e-12

    original_bytes = output_path.read_bytes()

    with pytest.raises(FileExistsError):
        write_mono_wav(output_path, sampling_frequency, input_signal)

    assert output_path.read_bytes() == original_bytes


def test_cli_processing_and_invalid_gain(tmp_path):
    sampling_frequency = 44100
    time = np.arange(sampling_frequency) / sampling_frequency
    input_signal = 0.2 * np.sin(2 * np.pi * 200 * time)
    input_signal += 0.15 * np.sin(2 * np.pi * 50 * time)

    input_path = tmp_path / "input.wav"
    output_path = tmp_path / "output.wav"
    script_path = Path(__file__).resolve().with_name("audio_processor.py")
    input_data = np.rint(input_signal * 32768.0).astype(np.int16)
    wavfile.write(input_path, sampling_frequency, input_data)
    original_input_bytes = input_path.read_bytes()

    command = [sys.executable, str(script_path), str(input_path), str(output_path)]

    invalid_result = subprocess.run(command + ["--mid-gain-db", "25"], capture_output=True, text=True)

    assert invalid_result.returncode == 2
    assert "Incorrect gains provided." in invalid_result.stderr
    assert not output_path.exists()

    result = subprocess.run(command + ["--high-gain-db", "6"], capture_output=True, text=True)

    assert result.returncode == 0, result.stderr
    assert "Scaling factor:" in result.stdout

    loaded_rate, loaded_signal = read_mono_wav(output_path)
    expected_signal = remove_tonal_noise(input_data.astype(np.float64) / 32768.0, sampling_frequency, 50.0, 30.0)
    expected_signal = equalize_audio(expected_signal, sampling_frequency, 0.0, 0.0, 6.0)
    peak = np.max(np.abs(expected_signal))
    expected_factor = 0.99 / peak if peak > 0.99 else 1.0

    assert loaded_rate == sampling_frequency
    assert loaded_signal.shape == input_signal.shape
    assert np.max(np.abs(loaded_signal - expected_signal * expected_factor)) <= 0.5 / 32768.0 + 1e-12
    assert input_path.read_bytes() == original_input_bytes
