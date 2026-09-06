import numpy as np

from fourier_sampling_lab import (
    analyze_experiment,
    calculate_alias_frequency,
    calculate_rmse,
    calculate_sample_spectrum,
    classify_sampling,
    find_dominant_frequency,
    generate_signal,
    sinc_reconstruct,
)


def test_sampling_classification():
    assert classify_sampling(3, 12) == "Safe"
    assert classify_sampling(5, 10) == "Boundary"
    assert classify_sampling(7, 10) == "Unsafe"


def test_alias_frequency():
    assert calculate_alias_frequency(3, 12) == 3
    assert calculate_alias_frequency(5, 10) == 5
    assert calculate_alias_frequency(7, 10) == 3
    assert calculate_alias_frequency(12, 10) == 2


def test_safe_signal_generation():
    _, _, sample_time, sampled_signal = generate_signal(3, 12)

    assert len(sample_time) == 12
    assert np.allclose(
        sampled_signal[:5],
        [0, 1, 0, -1, 0],
    )


def test_safe_fft_detects_original_frequency():
    _, _, _, sampled_signal = generate_signal(3, 12)
    frequency_bins, amplitude_spectrum = calculate_sample_spectrum(
        sampled_signal,
        12,
    )

    dominant = find_dominant_frequency(
        frequency_bins,
        amplitude_spectrum,
    )

    assert np.isclose(dominant, 3)
    assert np.isclose(np.max(amplitude_spectrum), 1)


def test_boundary_signal_has_no_reliable_frequency():
    _, _, _, sampled_signal = generate_signal(5, 10)
    frequency_bins, amplitude_spectrum = calculate_sample_spectrum(
        sampled_signal,
        10,
    )

    dominant = find_dominant_frequency(
        frequency_bins,
        amplitude_spectrum,
    )

    assert dominant is None


def test_unsafe_fft_detects_alias():
    _, _, _, sampled_signal = generate_signal(
        7,
        10,
        phase=np.pi / 2,
    )
    frequency_bins, amplitude_spectrum = calculate_sample_spectrum(
        sampled_signal,
        10,
    )

    dominant = find_dominant_frequency(
        frequency_bins,
        amplitude_spectrum,
    )

    assert np.isclose(dominant, 3)


def test_sinc_passes_through_sample_values():
    _, _, sample_time, sampled_signal = generate_signal(3, 12)
    reconstructed_samples = sinc_reconstruct(
        sample_time,
        sample_time,
        sampled_signal,
    )

    assert np.allclose(reconstructed_samples, sampled_signal)


def test_safe_reconstruction_error_order():
    result = analyze_experiment("Safe", 3, 12, 0)

    assert result["sinc_rmse"] < result["linear_rmse"]
    assert result["linear_rmse"] < result["zoh_rmse"]


def test_rmse_is_zero_for_identical_signals():
    signal = np.array([1.0, 2.0, 3.0])
    assert calculate_rmse(signal, signal) == 0
