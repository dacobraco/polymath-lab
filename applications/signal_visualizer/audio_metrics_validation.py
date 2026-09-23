import subprocess
from pathlib import Path

import numpy as np

from audio_processor import read_mono_wav


if __name__ == "__main__":
    project_directory = Path(__file__).resolve().parent
    demo_directory = project_directory / "audio_processor_demo"
    executable_path = demo_directory / "audio_metrics.exe"

    if not executable_path.is_file():
        raise FileNotFoundError(f"Compile the C program first: {executable_path}")

    for filename in ["noisy.wav", "cleaned.wav", "equalized.wav"]:
        sampling_frequency, signal = read_mono_wav(demo_directory / filename)
        input_text = "\n".join(f"{sample:.17g}" for sample in signal)

        result = subprocess.run([str(executable_path)], input=input_text, capture_output=True, text=True, check=True)

        measurements = {}

        for line in result.stdout.splitlines():
            name, value = line.split(":", 1)
            measurements[name.strip()] = value.strip()

        c_sample_count = int(measurements["Samples"])
        c_rms = float(measurements["RMS"])
        c_peak = float(measurements["Peak"])

        python_rms = np.sqrt(np.mean(signal * signal))
        python_peak = np.max(np.abs(signal))

        rms_error = abs(c_rms - python_rms)
        peak_error = abs(c_peak - python_peak)

        assert c_sample_count == len(signal)
        assert np.isfinite(c_rms) and np.isfinite(c_peak)
        assert rms_error < 1e-10
        assert peak_error < 1e-10

        print(f"File: {filename}")
        print(f"Samples: {c_sample_count}")
        print(f"RMS:  C={c_rms:.12f}, Python={python_rms:.12f}")
        print(f"Peak: C={c_peak:.12f}, Python={python_peak:.12f}")
        print(f"RMS difference: {rms_error:.3e}")
        print(f"Peak difference: {peak_error:.3e}")
        print()

    for invalid_input in ["", "invalid", "nan"]:
        result = subprocess.run([str(executable_path)], input=invalid_input, capture_output=True, text=True)
        assert result.returncode == 1, f"Invalid input was not rejected: {invalid_input!r}"

    print("C invalid-input checks passed.")
    print("Python-C audio metrics verification passed.")
