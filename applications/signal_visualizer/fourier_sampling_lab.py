import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import interp1d


def classify_sampling(signal_frequency, sample_rate):
    nyquist_frequency = sample_rate / 2

    if np.isclose(signal_frequency, nyquist_frequency):
        return "Boundary"
    if signal_frequency < nyquist_frequency:
        return "Safe"
    return "Unsafe"


def generate_signal(
    signal_frequency,
    sample_rate,
    duration=1.0,
    reference_rate=2000,
    phase=0.0,
):
    sample_interval = 1 / sample_rate
    reference_time = np.arange(0, duration, 1 / reference_rate)
    sample_time = np.arange(0, duration, sample_interval)

    reference_signal = np.sin(
        2 * np.pi * signal_frequency * reference_time + phase
    )
    sampled_signal = np.sin(
        2 * np.pi * signal_frequency * sample_time + phase
    )

    return reference_time, reference_signal, sample_time, sampled_signal


def calculate_alias_frequency(signal_frequency, sample_rate):
    nyquist_frequency = sample_rate / 2
    wrapped_frequency = signal_frequency % sample_rate

    if wrapped_frequency > nyquist_frequency:
        return sample_rate - wrapped_frequency
    return wrapped_frequency


def calculate_sample_spectrum(sampled_signal, sample_rate):
    number_of_samples = len(sampled_signal)
    sample_interval = 1 / sample_rate

    complex_spectrum = np.fft.rfft(sampled_signal)
    frequency_bins = np.fft.rfftfreq(
        number_of_samples,
        d=sample_interval,
    )

    amplitude_spectrum = np.abs(complex_spectrum) / number_of_samples

    if number_of_samples % 2 == 0:
        amplitude_spectrum[1:-1] *= 2
    else:
        amplitude_spectrum[1:] *= 2

    return frequency_bins, amplitude_spectrum


def find_dominant_frequency(
    frequency_bins,
    amplitude_spectrum,
    tolerance=1e-10,
):
    if np.max(amplitude_spectrum) < tolerance:
        return None

    dominant_index = np.argmax(amplitude_spectrum)
    return frequency_bins[dominant_index]


def sinc_reconstruct(query_time, sample_time, sampled_signal):
    sample_interval = sample_time[1] - sample_time[0]
    reconstructed_signal = np.zeros_like(query_time, dtype=float)

    for sample_index in range(len(sample_time)):
        normalized_distance = (
            query_time - sample_time[sample_index]
        ) / sample_interval
        reconstructed_signal += sampled_signal[sample_index] * np.sinc(
            normalized_distance
        )

    return reconstructed_signal


def reconstruct_signals(reference_time, sample_time, sampled_signal):
    zoh_function = interp1d(
        sample_time,
        sampled_signal,
        kind="previous",
        bounds_error=False,
        fill_value=(sampled_signal[0], sampled_signal[-1]),
    )
    linear_function = interp1d(
        sample_time,
        sampled_signal,
        kind="linear",
        bounds_error=False,
        fill_value=(sampled_signal[0], sampled_signal[-1]),
    )

    zoh_signal = zoh_function(reference_time)
    linear_signal = linear_function(reference_time)
    sinc_signal = sinc_reconstruct(
        reference_time,
        sample_time,
        sampled_signal,
    )

    return zoh_signal, linear_signal, sinc_signal


def calculate_rmse(reference_signal, reconstructed_signal):
    return np.sqrt(np.mean((reference_signal - reconstructed_signal) ** 2))


def analyze_experiment(
    name,
    signal_frequency,
    sample_rate,
    phase,
    duration=1.0,
    reference_rate=2000,
):
    (
        reference_time,
        reference_signal,
        sample_time,
        sampled_signal,
    ) = generate_signal(
        signal_frequency,
        sample_rate,
        duration,
        reference_rate,
        phase,
    )

    status = classify_sampling(signal_frequency, sample_rate)
    alias_frequency = calculate_alias_frequency(signal_frequency, sample_rate)

    frequency_bins, amplitude_spectrum = calculate_sample_spectrum(
        sampled_signal,
        sample_rate,
    )
    dominant_frequency = find_dominant_frequency(
        frequency_bins,
        amplitude_spectrum,
    )

    zoh_signal, linear_signal, sinc_signal = reconstruct_signals(
        reference_time,
        sample_time,
        sampled_signal,
    )

    sinc_at_samples = sinc_reconstruct(
        sample_time,
        sample_time,
        sampled_signal,
    )

    return {
        "name": name,
        "signal_frequency": signal_frequency,
        "sample_rate": sample_rate,
        "phase": phase,
        "nyquist_frequency": sample_rate / 2,
        "status": status,
        "alias_frequency": alias_frequency,
        "dominant_frequency": dominant_frequency,
        "reference_time": reference_time,
        "reference_signal": reference_signal,
        "sample_time": sample_time,
        "sampled_signal": sampled_signal,
        "frequency_bins": frequency_bins,
        "amplitude_spectrum": amplitude_spectrum,
        "zoh_signal": zoh_signal,
        "linear_signal": linear_signal,
        "sinc_signal": sinc_signal,
        "zoh_rmse": calculate_rmse(reference_signal, zoh_signal),
        "linear_rmse": calculate_rmse(reference_signal, linear_signal),
        "sinc_rmse": calculate_rmse(reference_signal, sinc_signal),
        "sinc_sample_error": np.max(
            np.abs(sampled_signal - sinc_at_samples)
        ),
    }


def run_known_checks(results):
    assert classify_sampling(3, 12) == "Safe"
    assert classify_sampling(5, 10) == "Boundary"
    assert classify_sampling(7, 10) == "Unsafe"

    assert calculate_alias_frequency(3, 12) == 3
    assert calculate_alias_frequency(5, 10) == 5
    assert calculate_alias_frequency(7, 10) == 3
    assert calculate_alias_frequency(12, 10) == 2

    safe, boundary, unsafe = results

    assert np.isclose(safe["dominant_frequency"], 3)
    assert boundary["dominant_frequency"] is None
    assert np.isclose(unsafe["dominant_frequency"], 3)

    assert safe["sinc_rmse"] < safe["linear_rmse"]
    assert safe["linear_rmse"] < safe["zoh_rmse"]

    for result in results:
        assert result["sinc_sample_error"] < 1e-10

    print("All known-result checks passed.")


def print_report(results):
    for result in results:
        detected = result["dominant_frequency"]
        detected_text = "None" if detected is None else f"{detected:.1f} Hz"

        print()
        print(f"Case: {result['name']}")
        print(f"Original frequency: {result['signal_frequency']} Hz")
        print(f"Sampling frequency: {result['sample_rate']} Hz")
        print(f"Nyquist frequency: {result['nyquist_frequency']} Hz")
        print(f"Classification: {result['status']}")
        print(f"Calculated alias frequency: {result['alias_frequency']} Hz")
        print(f"FFT dominant frequency: {detected_text}")
        print(f"ZOH RMSE: {result['zoh_rmse']:.6f}")
        print(f"Linear RMSE: {result['linear_rmse']:.6f}")
        print(f"Sinc RMSE: {result['sinc_rmse']:.6f}")
        print(
            "Maximum sinc error at sample times: "
            f"{result['sinc_sample_error']:.3e}"
        )


def create_dashboard(results):
    figure, axes = plt.subplots(3, 3, figsize=(18, 12))

    for row, result in enumerate(results):
        time_axis = axes[row, 0]
        spectrum_axis = axes[row, 1]
        reconstruction_axis = axes[row, 2]

        time_axis.plot(
            result["reference_time"],
            result["reference_signal"],
            color="tab:blue",
            label=f"Original: {result['signal_frequency']} Hz",
        )
        time_axis.plot(
            result["sample_time"],
            result["sampled_signal"],
            marker="o",
            linestyle="none",
            color="black",
            label="Samples",
        )

        if result["status"] == "Unsafe":
            alias_reference = np.sin(
                2
                * np.pi
                * result["alias_frequency"]
                * result["reference_time"]
                + result["phase"]
            )
            time_axis.plot(
                result["reference_time"],
                alias_reference,
                color="tab:orange",
                linestyle="--",
                label=f"Alias: {result['alias_frequency']} Hz",
            )

        time_axis.set_title(
            f"{result['name']}: "
            f"f0={result['signal_frequency']} Hz, "
            f"fs={result['sample_rate']} Hz"
        )
        time_axis.set_xlabel("Time [s]")
        time_axis.set_ylabel("Amplitude")
        time_axis.grid(True)
        time_axis.legend()

        spectrum_axis.stem(
            result["frequency_bins"],
            result["amplitude_spectrum"],
            linefmt="C4-",
            markerfmt="C4o",
            basefmt=" ",
        )

        detected = result["dominant_frequency"]
        if detected is None:
            detected_text = "None"
        else:
            detected_text = f"{detected:.1f} Hz"
            spectrum_axis.axvline(
                detected,
                color="tab:red",
                linestyle="--",
                label=f"Detected: {detected_text}",
            )
            spectrum_axis.legend()

        spectrum_axis.set_title(f"Sample spectrum: {detected_text}")
        spectrum_axis.set_xlim(0, result["nyquist_frequency"] + 0.5)
        spectrum_axis.set_ylim(-0.05, 1.1)
        spectrum_axis.set_xlabel("Frequency [Hz]")
        spectrum_axis.set_ylabel("Normalized amplitude")
        spectrum_axis.grid(True)

        reconstruction_axis.plot(
            result["reference_time"],
            result["reference_signal"],
            color="black",
            linewidth=2,
            label="Original",
        )
        reconstruction_axis.plot(
            result["reference_time"],
            result["zoh_signal"],
            color="tab:red",
            label=f"ZOH: {result['zoh_rmse']:.3f}",
        )
        reconstruction_axis.plot(
            result["reference_time"],
            result["linear_signal"],
            color="tab:green",
            label=f"Linear: {result['linear_rmse']:.3f}",
        )
        reconstruction_axis.plot(
            result["reference_time"],
            result["sinc_signal"],
            color="tab:purple",
            label=f"Sinc: {result['sinc_rmse']:.3f}",
        )
        reconstruction_axis.plot(
            result["sample_time"],
            result["sampled_signal"],
            marker="o",
            linestyle="none",
            color="tab:blue",
            label="Samples",
        )
        reconstruction_axis.set_title(
            f"Reconstruction (legend shows RMSE)"
        )
        reconstruction_axis.set_xlabel("Time [s]")
        reconstruction_axis.set_ylabel("Amplitude")
        reconstruction_axis.grid(True)
        reconstruction_axis.legend(fontsize=8)

    figure.suptitle(
        "Fourier and Sampling Laboratory",
        fontsize=16,
    )
    figure.tight_layout(rect=[0, 0, 1, 0.97])


def main():
    experiment_cases = [
        ("Safe", 3, 12, 0),
        ("Boundary", 5, 10, 0),
        ("Unsafe", 7, 10, np.pi / 2),
    ]

    results = [
        analyze_experiment(
            name,
            signal_frequency,
            sample_rate,
            phase,
        )
        for name, signal_frequency, sample_rate, phase in experiment_cases
    ]

    run_known_checks(results)
    print_report(results)
    create_dashboard(results)
    plt.show()


if __name__ == "__main__":
    main()
    