import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import solve_ivp


natural_frequency = 5.0
input_value = 1.0
damping_ratios = [0.0, 0.2, 1.0, 2.0]

start_time = 0.0
end_time = 8.0
evaluation_times = np.linspace(start_time, end_time, 1601)


def second_order_derivative(time, state, damping_ratio):
    output = state[0]
    output_rate = state[1]

    output_acceleration = (
        natural_frequency**2 * (input_value - output)
        - 2.0 * damping_ratio * natural_frequency * output_rate
    )

    return [output_rate, output_acceleration]


def solve_step_response(damping_ratio):
    initial_state = [0.0, 0.0]

    solution = solve_ivp(
        second_order_derivative,
        (start_time, end_time),
        initial_state,
        args=(damping_ratio,),
        t_eval=evaluation_times,
        rtol=1e-9,
        atol=1e-12,
    )

    return solution


def calculate_settling_time(times, output, tolerance=0.02):
    error = np.abs(output - input_value)
    outside_indices = np.where(error > tolerance)[0]

    if len(outside_indices) == 0:
        return times[0]

    last_outside_index = outside_indices[-1]

    if last_outside_index == len(times) - 1:
        return None

    return times[last_outside_index + 1]


def frequency_response_magnitude(frequency_ratio, damping_ratio):
    magnitude = 1.0 / np.sqrt(
        (1.0 - frequency_ratio**2) ** 2
        + (2.0 * damping_ratio * frequency_ratio) ** 2
    )

    return magnitude


solutions = {}

print("SECOND-ORDER STEP RESPONSES")
print()

for damping_ratio in damping_ratios:
    solution = solve_step_response(damping_ratio)

    if not solution.success:
        raise RuntimeError(solution.message)

    solutions[damping_ratio] = solution

    output = solution.y[0]
    peak_index = np.argmax(output)
    peak_output = output[peak_index]
    peak_time = solution.t[peak_index]
    if damping_ratio == 0.0:
        peak_time = np.pi / natural_frequency
    overshoot_percent = max(0.0, (peak_output - input_value) / input_value * 100.0)
    if overshoot_percent < 1e-9:
        overshoot_percent = 0.0
    settling_time = calculate_settling_time(solution.t, output)

    print("Damping ratio:", damping_ratio)
    print("Peak output:", peak_output)

    if damping_ratio < 1.0:
        print("Peak time:", peak_time, "s")
    else:
        print("Peak time: no oscillatory peak")

    print("Overshoot:", overshoot_percent, "%")

    if settling_time is None:
        print("Settling time: response did not settle")
    else:
        print("Settling time:", settling_time, "s")

    print("Final output:", output[-1])
    print()


damping_ratio_for_check = 0.2
checked_output = solutions[damping_ratio_for_check].y[0]
numerical_peak = np.max(checked_output)
numerical_overshoot = (numerical_peak - input_value) / input_value * 100.0

theoretical_overshoot = np.exp(
    -damping_ratio_for_check
    * np.pi
    / np.sqrt(1.0 - damping_ratio_for_check**2)
) * 100.0

initial_derivative = second_order_derivative(0.0, [0.0, 0.0], 0.2)
equilibrium_derivative = second_order_derivative(0.0, [1.0, 0.0], 0.2)

assert np.allclose(initial_derivative, [0.0, 25.0])
assert np.allclose(equilibrium_derivative, [0.0, 0.0])
assert abs(numerical_overshoot - theoretical_overshoot) < 0.1

print("NUMERICAL VERIFICATION")
print()
print("Numerical overshoot for zeta = 0.2:", numerical_overshoot, "%")
print("Theoretical overshoot for zeta = 0.2:", theoretical_overshoot, "%")
print("Overshoot difference:", abs(numerical_overshoot - theoretical_overshoot), "%")
print("Core checks passed.")


frequency_ratios = np.logspace(-1.0, 1.0, 1200)
resonance_damping_ratios = [0.2, 1.0, 2.0]

print()
print("RESONANCE")
print()

for damping_ratio in resonance_damping_ratios:
    magnitude = frequency_response_magnitude(frequency_ratios, damping_ratio)

    if damping_ratio < 1.0 / np.sqrt(2.0):
        resonance_index = np.argmax(magnitude)
        resonance_ratio = frequency_ratios[resonance_index]
        resonance_frequency = resonance_ratio * natural_frequency
        resonance_magnitude = magnitude[resonance_index]

        print("Damping ratio:", damping_ratio)
        print("Resonance frequency:", resonance_frequency, "rad/s")
        print("Maximum magnitude:", resonance_magnitude)
    else:
        print("Damping ratio:", damping_ratio)
        print("No pronounced resonance peak.")

    print()


figure, axes = plt.subplots(1, 2, figsize=(14, 5))

for damping_ratio in damping_ratios:
    solution = solutions[damping_ratio]
    axes[0].plot(solution.t, solution.y[0], label=f"zeta = {damping_ratio}")

axes[0].axhline(input_value, color="black", linestyle="--", label="Target")
axes[0].set_title("Step responses")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Output y(t)")
axes[0].grid(True)
axes[0].legend()

for damping_ratio in resonance_damping_ratios:
    magnitude = frequency_response_magnitude(frequency_ratios, damping_ratio)
    axes[1].semilogx(frequency_ratios, magnitude, label=f"zeta = {damping_ratio}")

axes[1].axvline(1.0, color="black", linestyle="--", label="Natural frequency")
axes[1].set_title("Resonance and damping")
axes[1].set_xlabel("Frequency ratio ω / ωn")
axes[1].set_ylabel("Magnitude")
axes[1].set_ylim(0.0, 3.0)
axes[1].grid(True)
axes[1].legend()

plt.tight_layout()
plt.show()
