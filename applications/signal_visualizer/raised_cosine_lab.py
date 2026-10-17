"""PolyMath #118 — QPSK pulse shaping, Nyquist criterion, and matched filtering.

Run:
    python raised_cosine_lab.py
    python raised_cosine_lab.py --save-dir figures --no-show

Dependencies: numpy, scipy, matplotlib.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import fftconvolve

N_SYMBOLS = 12
SAMPLES_PER_SYMBOL = 16
BETA = 0.35
SPAN = 6  # Half-length of each raised-cosine pulse, in symbol periods.
N_FFT = 4096
SEED = 42


def raised_cosine(beta: float, span: int, sps: int) -> np.ndarray:
    """Sample the unit-symbol-period raised-cosine pulse on [-span, +span]."""
    if not 0 <= beta <= 1:
        raise ValueError("beta must be in [0, 1]")
    t = np.arange(-span * sps, span * sps + 1) / sps
    if beta == 0:
        return np.sinc(t)

    h = np.empty_like(t, dtype=float)
    at_singularity = np.isclose(np.abs(t), 1 / (2 * beta), atol=1e-12)
    other = ~at_singularity
    h[other] = (np.sinc(t[other]) * np.cos(np.pi * beta * t[other])
                / (1 - (2 * beta * t[other]) ** 2))
    # Removable singularity: limit at t = +/-1/(2*beta).
    h[at_singularity] = (beta / 2) * np.sin(np.pi / (2 * beta))
    return h


def root_raised_cosine(beta: float, span: int, sps: int) -> np.ndarray:
    """Unit-energy real, symmetric RRC FIR (symbol period T=1)."""
    if not 0 <= beta <= 1:
        raise ValueError("beta must be in [0, 1]")
    t = np.arange(-span * sps, span * sps + 1) / sps
    if beta == 0:
        h = np.sinc(t)
    else:
        h = np.empty_like(t, dtype=float)
        at_zero = np.isclose(t, 0, atol=1e-12)
        at_special = np.isclose(np.abs(t), 1 / (4 * beta), atol=1e-12)
        other = ~(at_zero | at_special)
        h[at_zero] = 1 + beta * (4 / np.pi - 1)
        h[at_special] = (beta / np.sqrt(2)) * (
            (1 + 2 / np.pi) * np.sin(np.pi / (4 * beta))
            + (1 - 2 / np.pi) * np.cos(np.pi / (4 * beta))
        )
        x = t[other]
        h[other] = (np.sin(np.pi * x * (1 - beta))
                    + 4 * beta * x * np.cos(np.pi * x * (1 + beta))) / (
                        np.pi * x * (1 - (4 * beta * x) ** 2)
                    )
    return h / np.sqrt(np.sum(h ** 2))


def magnitude_db(signal: np.ndarray, n_fft: int = N_FFT) -> np.ndarray:
    spectrum = np.fft.fftshift(np.fft.fft(signal, n=n_fft))
    mag = np.abs(spectrum)
    return 20 * np.log10(mag / mag.max() + 1e-12)


def main(save_dir: Path | None = None, show: bool = True) -> None:
    rng = np.random.default_rng(SEED)
    bits = rng.integers(0, 2, size=(N_SYMBOLS, 2))
    symbols = ((2 * bits[:, 0] - 1) + 1j * (2 * bits[:, 1] - 1)) / np.sqrt(2)

    upsampled = np.zeros(N_SYMBOLS * SAMPLES_PER_SYMBOL, dtype=complex)
    upsampled[::SAMPLES_PER_SYMBOL] = symbols

    # The first 12*T seconds of the rectangular pulse-shaped waveform.
    rectangular = np.convolve(upsampled, np.ones(SAMPLES_PER_SYMBOL), mode="full")
    rectangular = rectangular[:N_SYMBOLS * SAMPLES_PER_SYMBOL]

    rc = raised_cosine(BETA, SPAN, SAMPLES_PER_SYMBOL)
    rc_signal = np.convolve(upsampled, rc, mode="full")
    rc_delay = (len(rc) - 1) // 2
    symbol_indices = rc_delay + np.arange(N_SYMBOLS) * SAMPLES_PER_SYMBOL
    rc_samples = rc_signal[symbol_indices]
    rc_error = np.max(np.abs(rc_samples - symbols))

    rrc = root_raised_cosine(BETA, SPAN, SAMPLES_PER_SYMBOL)
    transmitted = fftconvolve(upsampled, rrc, mode="full")
    received = fftconvolve(transmitted, np.conj(rrc[::-1]), mode="full")
    total_delay = len(rrc) - 1
    received_indices = total_delay + np.arange(N_SYMBOLS) * SAMPLES_PER_SYMBOL
    recovered = received[received_indices]
    rrc_error = np.max(np.abs(recovered - symbols))
    recovered_bits = np.column_stack((recovered.real > 0, recovered.imag > 0)).astype(int)
    bit_errors = np.count_nonzero(bits != recovered_bits)

    assert np.allclose(rc_samples, symbols, atol=1e-12)
    assert bit_errors == 0, "Unexpected bit error in noiseless QPSK model"

    print("PolyMath #118 — QPSK Pulse Shaping and Matched Filter")
    print(f"Symbols: {N_SYMBOLS}; bits: {bits.size}; samples/symbol: {SAMPLES_PER_SYMBOL}")
    print(f"RC (ideal Nyquist sampling) maximum symbol error: {rc_error:.8g}")
    print(f"RRC + matched filter maximum symbol error: {rrc_error:.12f}")
    print(f"Bit errors: {bit_errors} / {bits.size}")
    print("Original QPSK symbols:", symbols[:5])
    print("Matched-filter samples:", recovered[:5])

    freq = np.fft.fftshift(np.fft.fftfreq(N_FFT, d=1 / SAMPLES_PER_SYMBOL))
    figures = []

    fig, ax = plt.subplots(figsize=(11, 4))
    times = np.arange(len(rectangular)) / SAMPLES_PER_SYMBOL
    ax.step(times, rectangular.real, where="post", label="I component")
    ax.step(times, rectangular.imag, where="post", label="Q component", alpha=0.7)
    ax.set(xlabel="Time (symbol periods)", ylabel="Amplitude",
           title="QPSK with rectangular pulse shaping")
    ax.grid(True); ax.legend(); figures.append(("01_rectangular_qpsk.png", fig))

    fig, ax = plt.subplots(figsize=(11, 4))
    pulse_times = (np.arange(len(rc)) - rc_delay) / SAMPLES_PER_SYMBOL
    ax.plot(pulse_times, rc)
    ax.set(xlabel="Time (symbol periods)", ylabel="Amplitude",
           title=f"Raised-cosine pulse (roll-off beta = {BETA})")
    ax.grid(True); figures.append(("02_raised_cosine_pulse.png", fig))

    fig, ax = plt.subplots(figsize=(11, 4))
    rc_times = (np.arange(len(rc_signal)) - rc_delay) / SAMPLES_PER_SYMBOL
    ax.plot(rc_times, rc_signal.real, label="RC-shaped I component")
    ax.scatter(np.arange(N_SYMBOLS), rc_samples.real,
               color="tab:red", zorder=3, label="Nyquist sampling instants")
    ax.set(xlabel="Time (symbol periods)", ylabel="I amplitude",
           title="Raised-cosine QPSK: zero ISI at sampling instants")
    ax.grid(True); ax.legend(); figures.append(("03_rc_nyquist_samples.png", fig))

    fig, ax = plt.subplots(figsize=(11, 5))
    ax.plot(freq, magnitude_db(rectangular), label="Rectangular", alpha=0.8)
    ax.plot(freq, magnitude_db(rc_signal), label="Raised-Cosine", alpha=0.8)
    edge = (1 + BETA) / 2  # Cycles per symbol; T=1.
    ax.axvline(-edge, color="gray", ls="--", alpha=0.6)
    ax.axvline(edge, color="gray", ls="--", alpha=0.6,
               label=f"Ideal RC boundaries (+/-{edge:.3f})")
    ax.set(xlim=(-3, 3), ylim=(-90, 5), xlabel="Frequency (cycles per symbol)",
           ylabel="Normalized magnitude (dB)",
           title="Rectangular vs. raised-cosine spectrum (12 symbols)")
    ax.grid(True); ax.legend(); figures.append(("04_spectrum_comparison.png", fig))

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(symbols.real, symbols.imag, marker="x", s=90, label="Transmitted")
    ax.scatter(recovered.real, recovered.imag, facecolors="none", edgecolors="tab:orange",
               s=90, label="Matched-filter samples")
    ax.axhline(0, color="gray", lw=0.8); ax.axvline(0, color="gray", lw=0.8)
    ax.set(xlim=(-1.1, 1.1), ylim=(-1.1, 1.1), xlabel="I", ylabel="Q",
           title="QPSK detection after RRC matched filter")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True); ax.legend(); figures.append(("05_matched_filter_constellation.png", fig))

    for name, fig in figures:
        fig.tight_layout()
        if save_dir is not None:
            save_dir.mkdir(parents=True, exist_ok=True)
            fig.savefig(save_dir / name, dpi=160)
    if show:
        plt.show()
    else:
        plt.close("all")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--save-dir", type=Path, help="Optional directory to save PNG figures")
    parser.add_argument("--no-show", action="store_true", help="Do not open Matplotlib windows")
    args = parser.parse_args()
    main(save_dir=args.save_dir, show=not args.no_show)
