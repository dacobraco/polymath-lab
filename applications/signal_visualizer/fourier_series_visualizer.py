import numpy as np
import matplotlib.pyplot as plt

from fourier_utils import (
    generate_ideal_signal,
    calculate_fourier_coefficients,
    reconstruct_signal,
    calculate_rmse,
    calculate_spectrum,
)


def plot_results(
    theta,
    ideal_signal,
    reconstructed_signal,
    amplitudes,
    phases,
    signal_type,
    harmonic_num,
    rmse,
):
    harmonics = np.arange(1, harmonic_num + 1)

    fig, axes = plt.subplots(3, 1, figsize=(10, 10))

    axes[0].plot(
        theta,
        ideal_signal,
        color="black",
        linewidth=2,
        label="Ideal Signal",
    )

    axes[0].plot(
        theta,
        reconstructed_signal,
        color="blue",
        linewidth=1.5,
        label="Fourier Reconstruction",
    )

    axes[0].set_title(
        f"{signal_type.capitalize()} Signal Reconstruction "
        f"(N = {harmonic_num}, RMSE = {rmse:.4f})"
    )
    axes[0].set_xlabel("Phase [rad]")
    axes[0].set_ylabel("Amplitude")
    axes[0].legend()
    axes[0].grid(True)

    axes[1].stem(
        harmonics,
        amplitudes,
        basefmt=" ",
    )
    axes[1].set_title("Amplitude Spectrum")
    axes[1].set_xlabel("Harmonic Number")
    axes[1].set_ylabel("Amplitude")
    axes[1].set_xticks(harmonics)
    axes[1].grid(True)

    axes[2].stem(
        harmonics,
        phases,
        basefmt=" ",
    )
    axes[2].set_title("Phase Spectrum")
    axes[2].set_xlabel("Harmonic Number")
    axes[2].set_ylabel("Phase [deg]")
    axes[2].set_xticks(harmonics)
    axes[2].grid(True)

    plt.tight_layout()
    plt.show()


def main():
    try:
        signal_type = input(
            "Square or sawtooth signal? "
        ).strip().lower()

        harmonic_num = int(
            input("How many harmonics? ")
        )

        theta = np.linspace(
            -2 * np.pi,
            2 * np.pi,
            2000,
            endpoint=False,
        )

        ideal_signal = generate_ideal_signal(
            signal_type,
            theta,
        )

        a0, an, bn = calculate_fourier_coefficients(
            signal_type,
            harmonic_num,
        )

        reconstructed_signal = reconstruct_signal(
            theta,
            a0,
            an,
            bn,
        )

        rmse = calculate_rmse(
            ideal_signal,
            reconstructed_signal,
        )

        amplitudes, phases = calculate_spectrum(
            an,
            bn,
        )

        print(f"RMSE: {rmse}")
        print(f"Amplitudes: {amplitudes}")
        print(f"Phases: {phases}")

        plot_results(
            theta,
            ideal_signal,
            reconstructed_signal,
            amplitudes,
            phases,
            signal_type,
            harmonic_num,
            rmse,
        )

    except ValueError as error:
        print(f"Error: {error}")


if __name__ == "__main__":
    main()
