import numpy as np


N = 4

dft_matrix = np.zeros((N, N), dtype=complex)

for k in range(N):
    for n in range(N):
        dft_matrix[k, n] = np.exp(-2j * np.pi * k * n / N)

print("DFT matrix:")
print(dft_matrix)

signal = np.array([1, 0, -1, 0], dtype=complex)

spectrum = dft_matrix @ signal
numpy_spectrum = np.fft.fft(signal)

print("\nSignal:")
print(signal)

print("\nDFT from matrix:")
print(spectrum)

print("\nNumPy FFT:")
print(numpy_spectrum)

print("\nDifference:")
print(spectrum - numpy_spectrum)

print("\nMatrix DFT matches NumPy FFT:", np.allclose(spectrum, numpy_spectrum))

phase_signal = np.array([0, 1, 0, -1], dtype=complex)

phase_spectrum = dft_matrix @ phase_signal

print("\nPhase signal:")
print(phase_signal)

print("\nPhase signal spectrum:")
print(phase_spectrum)

print("\nMagnitudes:")
print(np.abs(phase_spectrum))

print("\nPhases [deg]:")
print(np.angle(phase_spectrum, deg=True))
