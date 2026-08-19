import numpy as np
import matplotlib.pyplot as plt

def numerical_fourier_transform(t, x, frequencies):
    X = np.zeros(len(frequencies), dtype=complex)

    for i, f in enumerate(frequencies):
        complex_exponent = - 1j * 2 * np.pi * f * t
        integrand = x * np.exp(complex_exponent)
        X[i] = np.trapezoid(integrand, t)

    return X

if __name__ == "__main__":

    t = np.linspace(-5, 5, 5001)
    frequencies = np.linspace(-5, 5, 501)
    x1 = np.exp(-np.pi * t**2)
    x2 = np.exp(-2 * np.pi * t**2)
    y = 2 * x1 - 3 * x2

    X1 = numerical_fourier_transform(t, x1, frequencies)
    X2 = numerical_fourier_transform(t, x2, frequencies)
    Y_direct = numerical_fourier_transform(t, y, frequencies)
    Y_linear = 2 * X1 - 3 * X2

    print("Linearity:", np.allclose(Y_linear, Y_direct, atol=1e-10))

    x_dual = np.exp(-np.pi * (t - 1)**2)
    X_dual = numerical_fourier_transform(t, x_dual, frequencies)
    XX_dual = numerical_fourier_transform(frequencies, X_dual, t)
    x_reflected = np.exp(-np.pi * (t + 1)**2)  # x(-t)

    print("Duality:", np.allclose(XX_dual, x_reflected, atol=1e-10))
