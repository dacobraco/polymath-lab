import numpy as np
import matplotlib.pyplot as plt

def one_pole_iir(input_signal, alpha):
    output_signal = np.zeros_like(input_signal, dtype=float)

    output_signal[0] = (1 - alpha) * input_signal[0]

    for n in range(1, len(input_signal)):
        output_signal[n] = (1 - alpha) * input_signal[n] + alpha * output_signal[n - 1]

    return output_signal

impulse = np.array([1.0, 0.0, 0.0, 0.0, 0.0, 0.0])
alpha = 0.5

impulse_response = one_pole_iir(impulse, alpha)

print("Impulse response:")
print(impulse_response)

step_signal = np.ones(10)

output_alpha_05 = one_pole_iir(step_signal, alpha)

print("Step response for alpha = 0.5:")
print(output_alpha_05)

new_alpha = 0.9

output_alpha_09 = one_pole_iir(step_signal, new_alpha)

print("Step response for alpha = 0.9:")
print(output_alpha_09)

sampling_frequency = 100
signal_frequency = 2.0
duration = 2.0

time = np.arange(0, duration, 1 / sampling_frequency)

s = np.sin(2 * np.pi * signal_frequency * time)

rng = np.random.default_rng(42)

noise = rng.normal(0.0, 0.5, len(s))

noisy_signal = s + noise

rmse_before = np.sqrt(np.mean((noisy_signal - s) ** 2))

print("RMSE before filtering:", rmse_before)

alphas = [0.2, 0.5, 0.7, 0.9]

for alpha in alphas:
    filtered_signal = one_pole_iir(noisy_signal, alpha)

    rmse_after = np.sqrt(np.mean((filtered_signal - s) ** 2))

    print("Alpha:", alpha, "RMSE after:", rmse_after)

alpha = 0.7

zero = 0.0
pole = alpha

angles = np.linspace(0, 2 * np.pi, 200)

unit_circle_x = np.cos(angles)
unit_circle_y = np.sin(angles)

plt.figure(figsize=(6, 6))

plt.plot(unit_circle_x, unit_circle_y, "--", label="Unit circle")

plt.scatter(zero, 0, marker="o", s=100, label="Zero")
plt.scatter(pole, 0, marker="x", s=100, label="Pole")

plt.axhline(0)
plt.axvline(0)

plt.xlabel("Real part")
plt.ylabel("Imaginary part")

plt.title("One-Pole IIR Pole-Zero Diagram")

plt.axis("equal")
plt.grid()
plt.legend()

plt.show()

omega = np.linspace(0, np.pi, 500)
frequency_hz = omega * sampling_frequency / (2 * np.pi)
target_magnitude = 1 / np.sqrt(2)

for alpha in alphas:
    magnitude = (1 - alpha) / np.sqrt(1 + alpha**2 - 2 * alpha * np.cos(omega))

    cutoff_index = np.argmin(np.abs(magnitude - target_magnitude))

    cutoff_frequency = frequency_hz[cutoff_index]

    print("Alpha:", alpha, "Cutoff frequency:", cutoff_frequency)

alpha = 0.7

magnitude = (1 - alpha) / np.sqrt(1 + alpha**2 - 2 * alpha * np.cos(omega))
cutoff_index = np.argmin(np.abs(magnitude - target_magnitude))
cutoff_frequency = frequency_hz[cutoff_index]

print("Target magnitude:", target_magnitude)
print("Cutoff frequency for alpha = 0.7:", cutoff_frequency)

plt.figure(figsize=(8, 5))

plt.plot(frequency_hz, magnitude, label="Magnitude response")

plt.axhline(target_magnitude, linestyle="--", label="-3 dB magnitude")
plt.axvline(cutoff_frequency, linestyle="--", label="Cutoff frequency")

plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")

plt.title("One-Pole IIR Frequency Response")

plt.grid()
plt.legend()

plt.show()
