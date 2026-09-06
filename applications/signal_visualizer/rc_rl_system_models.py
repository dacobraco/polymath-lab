import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

time = sp.symbols("t", real=True)
resistance, capacitance = sp.symbols("R C", positive=True)
input_voltage = sp.symbols("V_in", real=True)

capacitor_voltage = sp.Function("v_C")
derivative = sp.diff(capacitor_voltage(time), time)

rc_equation = sp.Eq(resistance * capacitance * derivative + capacitor_voltage(time), input_voltage)

print(rc_equation)

general_solution = sp.dsolve(rc_equation, capacitor_voltage(time))

print(general_solution)

initial_conditions = {
    capacitor_voltage(0): 0,
}

particular_solution = sp.dsolve(rc_equation, capacitor_voltage(time), ics=initial_conditions)

print(particular_solution)

parameter_values = {
    resistance: 10000,
    capacitance: 100e-6,
    input_voltage: 5,
}

time_constant = resistance * capacitance

numeric_time_constant = time_constant.subs(parameter_values)

voltage_expression = particular_solution.rhs
numeric_voltage_expression = voltage_expression.subs(parameter_values)

print("Time constant:", numeric_time_constant, "s")
print("Voltage expression:", numeric_voltage_expression)

measurement_times = [0, 1, 2, 5]

for time_value in measurement_times:
    voltage_value = numeric_voltage_expression.subs(time, time_value).evalf()
    print(f"Voltage at {time_value} s: {voltage_value} V")

rc_residual = sp.simplify(resistance * capacitance * sp.diff(voltage_expression, time) + voltage_expression - input_voltage)

print("RC equation residual:", rc_residual)

inductance = sp.symbols("L", positive=True)
current = sp.Function("i")

rl_equation = sp.Eq(inductance * sp.diff(current(time), time) + resistance * current(time), input_voltage)

general_rl_solution = sp.dsolve(rl_equation, current(time))

rl_initial_conditions = {
    current(0): 0,
}

particular_rl_solution = sp.dsolve(rl_equation, current(time), ics=rl_initial_conditions)

rl_current_expression = particular_rl_solution.rhs

rl_parameter_values = {
    resistance: 10,
    inductance: 0.5,
    input_voltage: 10,
}

rl_time_constant = inductance / resistance
numeric_rl_time_constant = rl_time_constant.subs(rl_parameter_values)
numeric_current_expression = rl_current_expression.subs(rl_parameter_values)

print("RL equation:", rl_equation)
print("General RL solution:", general_rl_solution)
print("Particular RL solution:", particular_rl_solution)
print("RL time constant:", numeric_rl_time_constant, "s")
print("Current expression:", numeric_current_expression)

rl_measurement_times = [0, 0.05, 0.10, 0.25]

for time_value in rl_measurement_times:
    current_value = numeric_current_expression.subs(time, time_value).evalf()
    print(f"Current at {time_value} s:", current_value, "A")

rl_residual = sp.simplify(inductance * sp.diff(rl_current_expression, time) + resistance * rl_current_expression - input_voltage)

print("RL equation residual:", rl_residual)

rc_numeric_function = sp.lambdify(time, numeric_voltage_expression, "numpy")
rl_numeric_function = sp.lambdify(time, numeric_current_expression, "numpy")

rc_time_values = np.linspace(0, 5 * float(numeric_time_constant), 1000)
rl_time_values = np.linspace(0, 5 * float(numeric_rl_time_constant), 1000)

rc_voltage_values = rc_numeric_function(rc_time_values)
rl_current_values = rl_numeric_function(rl_time_values)

fig, axes = plt.subplots(2, 1, figsize=(10, 8))

axes[0].plot(rc_time_values, rc_voltage_values, color="tab:blue", label="Capacitor Voltage")
axes[0].axhline(5, color="black", linestyle="--", label="Final Voltage")
axes[0].set_title("RC Step Response")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("Voltage [V]")
axes[0].legend()
axes[0].grid(True)

axes[1].plot(rl_time_values, rl_current_values, color="tab:orange", label="Inductor Current")
axes[1].axhline(1, color="black", linestyle="--", label="Final Current")
axes[1].set_title("RL Step Response")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("Current [A]")
axes[1].legend()
axes[1].grid(True)

rc_normalized_time = rc_time_values / float(numeric_time_constant)
rl_normalized_time = rl_time_values / float(numeric_rl_time_constant)

rc_normalized_response = rc_voltage_values / 5
rl_normalized_response = rl_current_values / 1

assert rc_residual == 0
assert rl_residual == 0

assert np.isclose(float(numeric_time_constant), 1.0)
assert np.isclose(float(numeric_rl_time_constant), 0.05)

assert np.isclose(float(numeric_voltage_expression.subs(time, 0)), 0.0)
assert np.isclose(float(numeric_current_expression.subs(time, 0)), 0.0)

assert np.allclose(rc_normalized_time, rl_normalized_time)
assert np.allclose(rc_normalized_response, rl_normalized_response)

print("All RC/RL model checks passed.")

fig.tight_layout()

plt.figure(figsize=(10, 5))
plt.plot(rc_normalized_time, rc_normalized_response, color="tab:blue", linewidth=2, label="Normalized RC Response")
plt.plot(rl_normalized_time, rl_normalized_response, color="tab:orange", linestyle="--", linewidth=2, label="Normalized RL Response")
plt.axhline(1, color="black", linestyle=":", label="Final Normalized Value")
plt.title("Normalized First-Order System Responses")
plt.xlabel("Normalized Time t/tau")
plt.ylabel("Normalized Response")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
