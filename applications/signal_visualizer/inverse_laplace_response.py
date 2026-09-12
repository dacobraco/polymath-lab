import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

s, t = sp.symbols("s t", positive=True)

first_order_system = 2 / (s + 2)
second_order_system = 9 / (s**2 + 2*s + 10)

first_order_impulse = sp.inverse_laplace_transform(first_order_system, s, t)
first_order_step = sp.inverse_laplace_transform(first_order_system / s, s, t)

second_order_impulse = sp.inverse_laplace_transform(second_order_system, s, t)
second_order_step = sp.inverse_laplace_transform(second_order_system / s, s, t)

print("First-order system")
print("H(s) =", first_order_system)
print("Impulse response =", sp.simplify(first_order_impulse))
print("Step response =", sp.simplify(first_order_step))

print("\nSecond-order system")
print("H(s) =", second_order_system)
print("Impulse response =", sp.simplify(second_order_impulse))
print("Step response =", sp.simplify(second_order_step))

expected_first_order_impulse = 2 * sp.exp(-2 * t)
expected_first_order_step = 1 - sp.exp(-2 * t)

expected_second_order_impulse = 3 * sp.exp(-t) * sp.sin(3 * t)

expected_second_order_step = (
    sp.Rational(9, 10)
    - sp.Rational(3, 10) * sp.exp(-t) * sp.sin(3 * t)
    - sp.Rational(9, 10) * sp.exp(-t) * sp.cos(3 * t)
)

assert sp.simplify(first_order_impulse - expected_first_order_impulse) == 0
assert sp.simplify(first_order_step - expected_first_order_step) == 0

assert sp.simplify(second_order_impulse - expected_second_order_impulse) == 0
assert sp.simplify(second_order_step - expected_second_order_step) == 0

print("\nAll inverse-Laplace symbolic checks passed.")
first_order_final_value = sp.limit(first_order_step, t, sp.oo)
second_order_final_value = sp.limit(second_order_step, t, sp.oo)

first_order_dc_gain = sp.simplify(first_order_system.subs(s, 0))
second_order_dc_gain = sp.simplify(second_order_system.subs(s, 0))

print("\nFinal-value checks")
print("First-order step final value =", first_order_final_value)
print("First-order DC gain =", first_order_dc_gain)

print("Second-order step final value =", second_order_final_value)
print("Second-order DC gain =", second_order_dc_gain)

assert first_order_final_value == first_order_dc_gain
assert second_order_final_value == second_order_dc_gain

print("Final values match DC gains.")

time_values = np.linspace(0, 6, 1000)

first_order_impulse_function = sp.lambdify(t, first_order_impulse, "numpy")
first_order_step_function = sp.lambdify(t, first_order_step, "numpy")

second_order_impulse_function = sp.lambdify(t, second_order_impulse, "numpy")
second_order_step_function = sp.lambdify(t, second_order_step, "numpy")

first_order_impulse_values = first_order_impulse_function(time_values)
first_order_step_values = first_order_step_function(time_values)

second_order_impulse_values = second_order_impulse_function(time_values)
second_order_step_values = second_order_step_function(time_values)

figure, axes = plt.subplots(2, 2, figsize=(12, 8))

axes[0, 0].plot(time_values, first_order_impulse_values)
axes[0, 0].set_title("First-Order Impulse Response")
axes[0, 0].set_xlabel("Time [s]")
axes[0, 0].set_ylabel("h(t)")
axes[0, 0].grid(True)

axes[0, 1].plot(time_values, first_order_step_values)
axes[0, 1].axhline(float(first_order_dc_gain), linestyle="--", label="DC gain")
axes[0, 1].set_title("First-Order Step Response")
axes[0, 1].set_xlabel("Time [s]")
axes[0, 1].set_ylabel("y(t)")
axes[0, 1].grid(True)
axes[0, 1].legend()

axes[1, 0].plot(time_values, second_order_impulse_values)
axes[1, 0].set_title("Second-Order Impulse Response")
axes[1, 0].set_xlabel("Time [s]")
axes[1, 0].set_ylabel("h(t)")
axes[1, 0].grid(True)

axes[1, 1].plot(time_values, second_order_step_values)
axes[1, 1].axhline(float(second_order_dc_gain), linestyle="--", label="DC gain")
axes[1, 1].set_title("Second-Order Step Response")
axes[1, 1].set_xlabel("Time [s]")
axes[1, 1].set_ylabel("y(t)")
axes[1, 1].grid(True)
axes[1, 1].legend()

figure.suptitle("Inverse Laplace: Impulse and Step Responses")
plt.tight_layout()
plt.show()

assert sp.simplify(first_order_impulse.subs(t, 0) - 2) == 0
assert sp.simplify(first_order_step.subs(t, 0)) == 0

assert sp.simplify(second_order_impulse.subs(t, 0)) == 0
assert sp.simplify(second_order_step.subs(t, 0)) == 0

assert sp.limit(first_order_impulse, t, sp.oo) == 0
assert sp.limit(second_order_impulse, t, sp.oo) == 0

assert sp.limit(first_order_step, t, sp.oo) == 1
assert sp.limit(second_order_step, t, sp.oo) == sp.Rational(9, 10)

print("\nInitial- and final-value checks passed.")
