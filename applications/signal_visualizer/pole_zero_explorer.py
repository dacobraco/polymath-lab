import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def find_poles(denominator_coefficients):
    return np.roots(denominator_coefficients)


def find_zeros(numerator_coefficients):
    if len(numerator_coefficients) == 1:
        return np.array([])

    return np.roots(numerator_coefficients)


numerator = [3]
denominator = [1, 4]

poles = find_poles(denominator)
zeros = find_zeros(numerator)

print("Numerator coefficients:", numerator)
print("Denominator coefficients:", denominator)
print("Poles:", poles)
print("Zeros:", zeros)

assert np.allclose(poles, [-4])
assert zeros.size == 0

print("First pole-zero checks passed.")

print("\nHigh-pass system")

high_pass_numerator = [1, 0]
high_pass_denominator = [1, 2]

high_pass_poles = find_poles(high_pass_denominator)
high_pass_zeros = find_zeros(high_pass_numerator)

print("Poles:", high_pass_poles)
print("Zeros:", high_pass_zeros)

assert np.allclose(high_pass_poles, [-2])
assert np.allclose(high_pass_zeros, [0])


print("\nStable oscillatory system")

oscillator_numerator = [25]
oscillator_denominator = [1, 2, 25]

oscillator_poles = find_poles(oscillator_denominator)
oscillator_zeros = find_zeros(oscillator_numerator)

print("Poles:", oscillator_poles)
print("Zeros:", oscillator_zeros)

assert np.all(np.real(oscillator_poles) < 0)
assert np.allclose(np.imag(oscillator_poles), [4.89897949, -4.89897949])

print("\nAdditional pole-zero checks passed.")

def plot_pole_zero_map(poles, zeros, title):
    plt.figure(figsize=(7, 6))

    plt.axhline(0, color="black", linewidth=1)
    plt.axvline(0, color="black", linewidth=1)

    if len(poles) > 0:
        plt.scatter(np.real(poles), np.imag(poles), color="red", marker="x", s=120, label="Poles")

    if len(zeros) > 0:
        plt.scatter(np.real(zeros), np.imag(zeros), facecolors="none", edgecolors="blue", marker="o", s=120, label="Zeros")

    plt.title(title)
    plt.xlabel("Real part")
    plt.ylabel("Imaginary part")
    plt.grid(True)
    plt.legend()
    plt.axis("equal")
    plt.tight_layout()
    plt.show()

print("\nUnstable oscillatory system")

unstable_numerator = [1]
unstable_denominator = [1, -1, 9.25]

unstable_poles = find_poles(unstable_denominator)
unstable_zeros = find_zeros(unstable_numerator)

print("Poles:", unstable_poles)
print("Zeros:", unstable_zeros)

assert np.allclose(np.real(unstable_poles), [0.5, 0.5])
assert np.allclose(np.imag(unstable_poles), [3, -3])
assert np.all(np.real(unstable_poles) > 0)

print("Unstable-system checks passed.")

def classify_stability(poles, tolerance=1e-9):
    real_parts = np.real(poles)

    if np.any(real_parts > tolerance):
        return "Unstable"

    if np.all(real_parts < -tolerance):
        return "Stable"

    return "Marginally stable"


boundary_numerator = [1]
boundary_denominator = [1, 0, 9]

boundary_poles = find_poles(boundary_denominator)
boundary_zeros = find_zeros(boundary_numerator)

print("\nStability classification")
print("Stable oscillator:", classify_stability(oscillator_poles))
print("Boundary oscillator:", classify_stability(boundary_poles))
print("Unstable oscillator:", classify_stability(unstable_poles))

assert classify_stability(oscillator_poles) == "Stable"
assert classify_stability(boundary_poles) == "Marginally stable"
assert classify_stability(unstable_poles) == "Unstable"

print("Stability-classification checks passed.")

def plot_system_comparison(systems):
    figure, axes = plt.subplots(2, 2, figsize=(12, 10))
    axes = axes.flatten()

    for axis, system in zip(axes, systems):
        title, poles, zeros = system
        stability = classify_stability(poles)

        axis.axvspan(-3, 0, color="green", alpha=0.08)
        axis.axvspan(0, 2, color="red", alpha=0.08)

        axis.axhline(0, color="black", linewidth=1)
        axis.axvline(0, color="black", linewidth=1)

        if len(poles) > 0:
            axis.scatter(np.real(poles), np.imag(poles), color="red", marker="x", s=120, label="Poles")

        if len(zeros) > 0:
            axis.scatter(np.real(zeros), np.imag(zeros), facecolors="none", edgecolors="blue", marker="o", s=120, label="Zeros")

        axis.set_title(f"{title}\n{stability}")
        axis.set_xlabel("Real part")
        axis.set_ylabel("Imaginary part")
        axis.set_xlim(-3, 2)
        axis.set_ylim(-6, 6)
        axis.grid(True)
        axis.legend()

    figure.suptitle("Pole-Zero Stability Comparison")
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.show()


comparison_systems = [
    ("High-pass system", high_pass_poles, high_pass_zeros),
    ("Stable oscillator", oscillator_poles, oscillator_zeros),
    ("Boundary oscillator", boundary_poles, boundary_zeros),
    ("Unstable oscillator", unstable_poles, unstable_zeros)
]

plot_system_comparison(comparison_systems)

time = np.linspace(0, 6, 2000)

response_cases = [
    ("Stable: -0.5 ± j3", -0.5, 3),
    ("Marginally stable: 0 ± j3", 0, 3),
    ("Unstable: 0.5 ± j3", 0.5, 3)
]

figure, axes = plt.subplots(3, 1, figsize=(11, 9), sharex=True)

for axis, response_case in zip(axes, response_cases):
    title, real_part, imaginary_part = response_case

    response = np.exp(real_part * time) * np.cos(imaginary_part * time)
    upper_envelope = np.exp(real_part * time)
    lower_envelope = -upper_envelope

    axis.plot(time, response, color="blue", label="System response")
    axis.plot(time, upper_envelope, color="red", linestyle="--", label="Amplitude envelope")
    axis.plot(time, lower_envelope, color="red", linestyle="--")

    axis.set_title(title)
    axis.set_ylabel("Amplitude")
    axis.grid(True)
    axis.legend()

axes[-1].set_xlabel("Time [s]")

figure.suptitle("How Pole Position Changes the Time Response")
plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

step_time = np.linspace(0, 3, 1000)

high_pass_transfer_function = signal.TransferFunction([1, 0], [1, 2])
low_pass_transfer_function = signal.TransferFunction([2], [1, 2])

high_pass_time, high_pass_response = signal.step(high_pass_transfer_function, T=step_time)
low_pass_time, low_pass_response = signal.step(low_pass_transfer_function, T=step_time)

step_input = np.ones_like(step_time)

plt.figure(figsize=(11, 6))

plt.plot(step_time, step_input, color="black", linestyle="--", label="Constant input")
plt.plot(high_pass_time, high_pass_response, color="blue", label="High-pass: s / (s + 2)")
plt.plot(low_pass_time, low_pass_response, color="red", label="Low-pass: 2 / (s + 2)")

plt.title("How a Zero at s = 0 Blocks a Constant Signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
