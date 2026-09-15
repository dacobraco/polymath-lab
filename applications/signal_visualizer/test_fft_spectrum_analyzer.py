import sys

import numpy as np
import pytest
import soundfile as sf

from fft_spectrum_analyzer import (
    calculate_amplitude_spectrum,
    find_dominant_frequency,
    load_wav,
    parse_arguments,
    select_segment,
)


def test_known_sine_amplitude_and_frequency():
    sample_rate = 1000
    duration = 1.0
    signal_frequency = 100.0
    signal_amplitude = 0.7

    sample_count = int(sample_rate * duration)
    time = np.arange(sample_count) / sample_rate
    signal = signal_amplitude * np.sin(2 * np.pi * signal_frequency * time)

    frequencies, amplitudes, frequency_resolution, original_mean = calculate_amplitude_spectrum(signal, sample_rate)

    dominant_index = np.argmax(amplitudes[1:]) + 1

    assert len(frequencies) == 501
    assert len(amplitudes) == 501
    assert np.isclose(frequency_resolution, 1.0)
    assert np.isclose(frequencies[dominant_index], 100.0)
    assert np.isclose(amplitudes[dominant_index], 0.7, atol=1e-3)
    assert np.isclose(original_mean, 0.0, atol=1e-12)


def test_dominant_frequency_respects_selected_range():
    frequencies = np.array([0.0, 50.0, 100.0, 150.0, 200.0])
    amplitudes = np.array([10.0, 0.1, 0.8, 0.4, 0.2])

    dominant_frequency, dominant_amplitude, dominant_index = find_dominant_frequency(
        frequencies, amplitudes, 20.0, 180.0
    )

    assert dominant_frequency == 100.0
    assert dominant_amplitude == 0.8
    assert dominant_index == 2


def test_select_segment_allows_exact_signal_end():
    signal = np.arange(10, dtype=float)
    sample_rate = 10

    segment, start_index, end_index = select_segment(signal, sample_rate, 0.5, 0.5)

    assert start_index == 5
    assert end_index == 10
    assert len(segment) == 5
    assert np.array_equal(segment, np.array([5.0, 6.0, 7.0, 8.0, 9.0]))


def test_select_segment_rejects_invalid_range():
    signal = np.arange(10, dtype=float)
    sample_rate = 10

    with pytest.raises(ValueError):
        select_segment(signal, sample_rate, -0.1, 0.5)

    with pytest.raises(ValueError):
        select_segment(signal, sample_rate, 1.0, 0.5)

    with pytest.raises(ValueError):
        select_segment(signal, sample_rate, 0.8, 0.5)


def test_amplitude_spectrum_rejects_invalid_signal():
    with pytest.raises(ValueError):
        calculate_amplitude_spectrum(np.array([[1.0, 2.0], [3.0, 4.0]]), 1000)

    with pytest.raises(ValueError):
        calculate_amplitude_spectrum(np.array([1.0, np.nan, 2.0]), 1000)

    with pytest.raises(ValueError):
        calculate_amplitude_spectrum(np.array([1.0]), 1000)


def test_load_wav_downmixes_stereo(tmp_path):
    sample_rate = 8000
    sample_count = 100
    time = np.arange(sample_count) / sample_rate

    left_channel = 0.6 * np.sin(2 * np.pi * 100 * time)
    right_channel = 0.2 * np.sin(2 * np.pi * 100 * time)
    stereo_signal = np.column_stack((left_channel, right_channel))

    wav_path = tmp_path / "stereo_test.wav"
    sf.write(wav_path, stereo_signal, sample_rate, subtype="FLOAT")

    mono_signal, loaded_sample_rate, channel_count, original_shape = load_wav(wav_path)

    expected_mono_signal = (left_channel + right_channel) / 2

    assert loaded_sample_rate == sample_rate
    assert channel_count == 2
    assert original_shape == (sample_count, 2)
    assert mono_signal.shape == (sample_count,)
    assert np.allclose(mono_signal, expected_mono_signal, atol=1e-7)


def test_parse_arguments(monkeypatch):
    command_line = [
        "fft_spectrum_analyzer.py",
        "recorded_voice.wav",
        "--start",
        "1",
        "--duration",
        "2",
        "--min-frequency",
        "60",
        "--max-frequency",
        "1200",
    ]

    monkeypatch.setattr(sys, "argv", command_line)

    args = parse_arguments()

    assert args.file_path == "recorded_voice.wav"
    assert args.start == 1.0
    assert args.duration == 2.0
    assert args.min_frequency == 60.0
    assert args.max_frequency == 1200.0


def test_complete_wav_analysis_pipeline(tmp_path):
    sample_rate = 1000
    duration = 1.0
    signal_frequency = 100.0
    signal_amplitude = 0.7

    sample_count = int(sample_rate * duration)
    time = np.arange(sample_count) / sample_rate
    original_signal = signal_amplitude * np.sin(2 * np.pi * signal_frequency * time)

    wav_path = tmp_path / "known_tone.wav"
    sf.write(wav_path, original_signal, sample_rate, subtype="FLOAT")

    loaded_signal, loaded_sample_rate, channel_count, original_shape = load_wav(wav_path)
    segment, start_index, end_index = select_segment(loaded_signal, loaded_sample_rate, 0.0, 1.0)
    frequencies, amplitudes, frequency_resolution, original_mean = calculate_amplitude_spectrum(
        segment, loaded_sample_rate
    )
    dominant_frequency, dominant_amplitude, dominant_index = find_dominant_frequency(
        frequencies, amplitudes, 20.0, 200.0
    )

    assert loaded_sample_rate == 1000
    assert channel_count == 1
    assert original_shape == (1000,)
    assert start_index == 0
    assert end_index == 1000
    assert len(segment) == 1000
    assert np.isclose(frequency_resolution, 1.0)
    assert np.isclose(original_mean, 0.0, atol=1e-7)
    assert np.isclose(dominant_frequency, 100.0)
    assert np.isclose(dominant_amplitude, 0.7, atol=1e-3)
    assert dominant_index == 100
