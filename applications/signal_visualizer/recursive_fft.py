import numpy as np

def recursive_fft(signal):
    N = len(signal)
    if N == 1:
        return signal
    even_signal = signal[::2]
    odd_signal = signal[1::2]

    even_fft = recursive_fft(even_signal)
    odd_fft = recursive_fft(odd_signal)

    spectrum = np.zeros(N, dtype=complex)

    for k in range (N//2):
        factor = np.exp(-1j*2*np.pi*k/N) * odd_fft[k]
        spectrum[k] = even_fft[k] + factor
        spectrum[k + N//2] = even_fft[k] - factor

    return spectrum

signal = np.array([1.0, 2.0, 3.0, 4.0], dtype=complex)
expected = np.array([10, -2+2j, -2, -2-2j], dtype=complex)

result = recursive_fft(signal)
numpy_result = np.fft.fft(signal)

print("Signal:", signal)
print("FFT signal:", result)
print("NumPy FFT:", numpy_result)
print("Expected FFT signal:", expected)
print("Results are matching:", np.allclose(result, expected))
print("Recursive FFT matches NumPy:", np.allclose(result, numpy_result))
print("NumPy FFT matches theory:", np.allclose(numpy_result, expected))

impulse = np.array([1, 0, 0, 0, 0, 0, 0, 0], dtype=complex)
expected_impulse = np.array([1, 1, 1, 1, 1, 1, 1, 1], dtype=complex)

impulse_result = recursive_fft(impulse)
numpy_impulse_result = np.fft.fft(impulse)

print("Impulse:", impulse)
print("FFT impulse:", impulse_result)
print("Expected FFT impulse:", expected_impulse)
print("Results are matching:", np.allclose(impulse_result, expected_impulse))
print("Recursive FFT matches NumPy:", np.allclose(impulse_result, numpy_impulse_result))
