import numpy as np
import matplotlib.pyplot as plt

f = 2  # Hz
t = np.linspace(0, 1, 1000)

theta = 2 * np.pi * f * t
complex_signal = np.exp(1j * theta)

real_part = complex_signal.real
imag_part = complex_signal.imag

plt.plot(t, real_part, label="Real part (cosine)")
plt.plot(t, imag_part, label="Imaginary part (sine)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Complex Exponential at f = 2 Hz")
plt.legend()
plt.grid(True)
plt.show()
