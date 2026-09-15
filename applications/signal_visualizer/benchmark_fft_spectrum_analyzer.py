import time
from statistics import median

import numpy as np

from fft_spectrum_analyzer import calculate_amplitude_spectrum


SAMPLE_RATE = 48000
SAMPLE_COUNTS = [1024, 4096, 16384, 65536, 262144]
REPETITIONS = 20


def measure_fft_time(signal, sample_rate, repetitions):
    calculate_amplitude_spectrum(signal, sample_rate)

    measured_times = []

    for _ in range(repetitions):
        start_time = time.perf_counter()
        calculate_amplitude_spectrum(signal, sample_rate)
        end_time = time.perf_counter()

        measured_times.append(end_time - start_time)

    return median(measured_times)


def main():
    random_generator = np.random.default_rng(65)

    print("FFT spectrum analyzer benchmark")
    print("Sample rate:", SAMPLE_RATE)
    print("Repetitions per size:", REPETITIONS)
    print()
    print(f"{'Samples':>10} {'Median [ms]':>15} {'Time/sample [ns]':>20}")

    for sample_count in SAMPLE_COUNTS:
        signal = random_generator.standard_normal(sample_count)

        median_time = measure_fft_time(signal, SAMPLE_RATE, REPETITIONS)
        median_time_ms = median_time * 1000
        time_per_sample_ns = median_time / sample_count * 1e9

        print(f"{sample_count:>10} {median_time_ms:>15.6f} {time_per_sample_ns:>20.3f}")


if __name__ == "__main__":
    main()
