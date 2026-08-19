import numpy as np
import matplotlib.pyplot as plt
from fourier_properties import numerical_fourier_transform

t = np.linspace(-5, 5, 5001)
frequencies = np.linspace(-5, 5, 501)

x = np.exp(-np.pi * t**2)
x_shifted = np.exp(-np.pi * (t - 2)**2)
X = numerical_fourier_transform(t, x, frequencies)
X_shifted = numerical_fourier_transform(t, x_shifted, frequencies)

X_shifted_predicted = X * np.exp(-1j * 4 * np.pi * frequencies)

magnitude_error = np.max(np.abs(np.abs(X_shifted) - np.abs(X)))
shift_error = np.max(np.abs(X_shifted - X_shifted_predicted))

print("Magnitude error:", magnitude_error)
print("Shift property error:", shift_error)

x_scaled = np.exp(-4 * np.pi * t**2)
X_scaled = numerical_fourier_transform(t, x_scaled, frequencies)

X_scaled_predicted = 1 / 2 * numerical_fourier_transform(t, x, frequencies / 2)

scale_error = np.max(np.abs(X_scaled - X_scaled_predicted))

print("Scale error:", scale_error)

f0 = 2

x_modulated = x * np.exp(1j * 2 * np.pi * f0 * t)
X_modulated = numerical_fourier_transform(t, x_modulated, frequencies)
X_modulated_predicted = numerical_fourier_transform(t, x, frequencies - f0)

modulation_error = np.max(np.abs(X_modulated - X_modulated_predicted))

print("Modulation error:", modulation_error)

x_cos_modulated = x * np.cos(2 * np.pi * f0 * t)
X_cos_modulated = numerical_fourier_transform(t, x_cos_modulated, frequencies)
X_cos_modulated_predicted = 1 / 2 * numerical_fourier_transform(t, x, frequencies - f0) + 1 / 2 * numerical_fourier_transform(t, x, frequencies + f0)

cos_modulation_error = np.max(np.abs(X_cos_modulated - X_cos_modulated_predicted))

print("Cosine modulation error:", cos_modulation_error)

fig, axes = plt.subplots(4, 2, figsize=(12, 16))

axes[0, 0].plot(t, x, label="Original")
axes[0, 0].plot(t, x_shifted, label="Shifted")
axes[0, 0].set_title("Time Shift - Time Domain")
axes[0, 0].set_xlabel("Time [s]")
axes[0, 0].set_ylabel("Amplitude")
axes[0, 0].grid(True)
axes[0, 0].legend()

axes[0, 1].plot(frequencies, np.abs(X), label="Original Spectrum")
axes[0, 1].plot(frequencies, np.abs(X_shifted), label="Shifted Spectrum")
axes[0, 1].set_title("Time Shift - Frequency Domain")
axes[0, 1].set_xlabel("Frequency [Hz]")
axes[0, 1].set_ylabel("Magnitude")
axes[0, 1].grid(True)
axes[0, 1].legend()

axes[1, 0].plot(t, x, label="Original")
axes[1, 0].plot(t, x_scaled, label="Scaled")
axes[1, 0].set_title("Time Scaling - Time Domain")
axes[1, 0].set_xlabel("Time [s]")
axes[1, 0].set_ylabel("Amplitude")
axes[1, 0].grid(True)
axes[1, 0].legend()

axes[1, 1].plot(frequencies, np.abs(X), label="Original Spectrum")
axes[1, 1].plot(frequencies, np.abs(X_scaled), label="Scaled Spectrum")
axes[1, 1].set_title("Time Scaling - Frequency Domain")
axes[1, 1].set_xlabel("Frequency [Hz]")
axes[1, 1].set_ylabel("Magnitude")
axes[1, 1].grid(True)
axes[1, 1].legend()

axes[2, 0].plot(t, x, label="Original")
axes[2, 0].plot(t, np.real(x_modulated), label="Real Part of Modulated Signal")
axes[2, 0].set_title("Complex Modulation - Time Domain")
axes[2, 0].set_xlabel("Time [s]")
axes[2, 0].set_ylabel("Amplitude")
axes[2, 0].grid(True)
axes[2, 0].legend()

axes[2, 1].plot(frequencies, np.abs(X), label="Original Spectrum")
axes[2, 1].plot(frequencies, np.abs(X_modulated), label="Modulated Spectrum")
axes[2, 1].set_title("Complex Modulation - Frequency Domain")
axes[2, 1].set_xlabel("Frequency [Hz]")
axes[2, 1].set_ylabel("Magnitude")
axes[2, 1].grid(True)
axes[2, 1].legend()

axes[3, 0].plot(t, x, label="Original")
axes[3, 0].plot(t, x_cos_modulated, label="Cosine Modulated")
axes[3, 0].set_title("Cosine Modulation - Time Domain")
axes[3, 0].set_xlabel("Time [s]")
axes[3, 0].set_ylabel("Amplitude")
axes[3, 0].grid(True)
axes[3, 0].legend()

axes[3, 1].plot(frequencies, np.abs(X), label="Original Spectrum")
axes[3, 1].plot(frequencies, np.abs(X_cos_modulated), label="Cosine Modulated Spectrum")
axes[3, 1].set_title("Cosine Modulation - Frequency Domain")
axes[3, 1].set_xlabel("Frequency [Hz]")
axes[3, 1].set_ylabel("Magnitude")
axes[3, 1].grid(True)
axes[3, 1].legend()

plt.tight_layout()
plt.show()
