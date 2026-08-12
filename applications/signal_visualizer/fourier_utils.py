import numpy as np

def generate_ideal_signal(signal_type, theta):
    if signal_type == "square":
        x = np.sign(np.sin(theta))
    elif signal_type == "sawtooth":
        theta_wrapped = (theta + np.pi) % (2 * np.pi) - np.pi
        x = theta_wrapped / np.pi
    else:
        raise ValueError("Unsupported signal type")
    return x

def calculate_fourier_coefficients(signal_type, harmonic_count):
    if harmonic_count <= 0:
        raise ValueError("Harmonic count must be positive")

    if signal_type not in ("square", "sawtooth"):
        raise ValueError("Unsupported signal type")

    a0 = 0.0
    an = np.zeros(harmonic_count, dtype=float)
    bn = np.zeros(harmonic_count, dtype=float)

    for n in range(1, harmonic_count + 1):
        if signal_type == "square":
            if n % 2 != 0:
                bn[n - 1] = 4 / (n * np.pi)

        elif signal_type == "sawtooth":
            bn[n - 1] = 2 * ((-1) ** (n + 1)) / (n * np.pi)

    return a0, an, bn

def reconstruct_signal(theta, a0, an, bn):
    if len(an) != len(bn):
        raise ValueError("Coefficient arrays must have the same length")

    x = np.full_like(theta, a0 / 2, dtype=float)
    for n in range(1, len(an) + 1):
        x += an[n - 1] * np.cos(n * theta) + bn[n - 1] * np.sin(n * theta)

    return x

def calculate_rmse(ideal_signal, reconstructed_signal):
    if ideal_signal.shape != reconstructed_signal.shape:
        raise ValueError("Signals must have the same shape")
    rmse = np.sqrt(np.mean((ideal_signal - reconstructed_signal) ** 2))
    return rmse

def calculate_spectrum(an, bn):
    if an.shape != bn.shape:
        raise ValueError("Coefficient arrays must have the same shape")
    amplitudes = np.sqrt(an ** 2 + bn ** 2)
    phases = np.degrees(np.atan2(-bn, an))
    return amplitudes, phases

if __name__ == "__main__":

    a0, an, bn = calculate_fourier_coefficients("sawtooth", 5)
    amplitudes, phases = calculate_spectrum(an, bn)

    print(amplitudes)
    print(phases)
