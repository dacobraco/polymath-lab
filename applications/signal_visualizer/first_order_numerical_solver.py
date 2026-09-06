from scipy.integrate import solve_ivp
import numpy as np
import matplotlib.pyplot as plt

input_voltage = 5.0
time_constant = 1.0


def rc_derivative(time, state):
    voltage = state[0]
    voltage_derivative = (input_voltage - voltage) / time_constant
    return [voltage_derivative]


print("Derivative at 0 V:", rc_derivative(0.0, [0.0]))
print("Derivative at 4 V:", rc_derivative(0.0, [4.0]))

evaluation_times = [0.0, 1.0, 2.0, 5.0]

solution = solve_ivp(rc_derivative, (0.0, 5.0), [0.0], t_eval=evaluation_times)

print("Solver success:", solution.success)
print("Solver message:", solution.message)
print("Solution times:", solution.t)
print("Numerical voltages:", solution.y[0])

numerical_voltages = solution.y[0]

theoretical_voltages = input_voltage * (1 - np.exp(-solution.t / time_constant))

absolute_errors = np.abs(theoretical_voltages - numerical_voltages)

maximum_error = np.max(absolute_errors)

print("Theoretical voltages:", theoretical_voltages)
print("Absolute errors:", absolute_errors)
print("Maximum absolute error:", maximum_error, "V")

strict_solution = solve_ivp(
    rc_derivative,
    (0.0, 5.0),
    [0.0],
    t_eval=evaluation_times,
    rtol=1e-9,
    atol=1e-12,
)

strict_numerical_voltages = strict_solution.y[0]

strict_theoretical_voltages = input_voltage * (1 - np.exp(-strict_solution.t / time_constant))

strict_absolute_errors = np.abs(strict_theoretical_voltages - strict_numerical_voltages)

strict_maximum_error = np.max(strict_absolute_errors)

print("Strict numerical voltages:", strict_numerical_voltages)
print("Strict absolute errors:", strict_absolute_errors)
print("Strict maximum error:", strict_maximum_error, "V")
print("Default function evaluations:", solution.nfev)
print("Strict function evaluations:", strict_solution.nfev)

plot_times = np.linspace(0.0, 5.0, 501)

plot_solution = solve_ivp(
    rc_derivative,
    (0.0, 5.0),
    [0.0],
    t_eval=plot_times,
    rtol=1e-9,
    atol=1e-12,
)

numerical_plot_voltages = plot_solution.y[0]

theoretical_plot_voltages = input_voltage * (1 - np.exp(-plot_times / time_constant))

plot_absolute_errors = np.abs(theoretical_plot_voltages - numerical_plot_voltages)

plot_maximum_error = np.max(plot_absolute_errors)

assert plot_solution.success
assert plot_maximum_error < 1e-8

print("Plot points:", len(plot_times))
print("Dense-grid maximum error:", plot_maximum_error, "V")
print("Dense-grid checks passed.")

fig, axes = plt.subplots(2, 1, figsize=(10, 7), sharex=True)

axes[0].plot(plot_times, theoretical_plot_voltages, color="black", label="Analytical Solution")
axes[0].plot(plot_times, numerical_plot_voltages, color="tab:blue", linestyle="--", label="Numerical Solution")
axes[0].set_title("RC Analytical and Numerical Step Responses")
axes[0].set_ylabel("Capacitor Voltage [V]")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(plot_times, plot_absolute_errors, color="tab:red", label="Absolute Error")
axes[1].set_title("Absolute Numerical Error")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Absolute Error [V]")
axes[1].legend()
axes[1].grid(True)

plt.tight_layout()
plt.show()
