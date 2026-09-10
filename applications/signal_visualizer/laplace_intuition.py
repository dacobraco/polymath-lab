import sympy as sp

t = sp.symbols("t", positive=True)
s = sp.symbols("s")

step_transform = sp.laplace_transform(1, t, s, noconds=True)

exponential_signal = sp.exp(-2*t)
exponential_transform = sp.laplace_transform(exponential_signal, t, s, noconds=True)

sine_signal = sp.sin(3*t)
sine_transform = sp.laplace_transform(sine_signal, t, s, noconds=True)

print("L{1} =", step_transform)
print("L{exp(-2t)} =", exponential_transform)
print("L{sin(3t)} =", sine_transform)

Y, U = sp.symbols("Y U")

laplace_equation = sp.Eq(s * Y  + 2 * Y, U)
output_solution = sp.solve(laplace_equation, Y)[0]
transfer_function = sp.simplify(output_solution / U)

print("Laplace equation:", laplace_equation)
print("Y(s) =", output_solution)
print("H(s) =", transfer_function)

zeta, omega_n = sp.symbols("ζ ω_n", positive=True)

second_order_equation = sp.Eq(s**2 * Y + 2 * zeta * omega_n * s * Y + omega_n**2 * Y, omega_n**2 * U)

second_order_output = sp.solve(second_order_equation, Y)[0]

second_order_transfer_function = sp.simplify(second_order_output / U)

print("Second-order Laplace equation:", second_order_equation)
print("Second-order Y(s) =", second_order_output)
print("Second-order H(s) =", second_order_transfer_function)

concrete_transfer_function = second_order_transfer_function.subs({
    zeta: 0.2,
    omega_n: 5,
})

dc_gain = sp.simplify(concrete_transfer_function.subs(s, 0))

step_output = sp.simplify(concrete_transfer_function * (1 / s))

print("Concrete H(s) =", concrete_transfer_function)
print("DC gain H(0) =", dc_gain)
print("Step output Y(s) =", step_output)

expected_step_transform = 1 / s
expected_exponential_transform = 1 / (s + 2)
expected_sine_transform = 3 / (s**2 + 9)
expected_first_order_transfer_function = 1 / (s + 2)

expected_second_order_transfer_function = (omega_n**2 / (s**2 + 2 * zeta * omega_n * s + omega_n**2))

assert sp.simplify(step_transform - expected_step_transform) == 0
assert sp.simplify(exponential_transform - expected_exponential_transform) == 0
assert sp.simplify(sine_transform - expected_sine_transform) == 0
assert sp.simplify(transfer_function - expected_first_order_transfer_function) == 0
assert sp.simplify(second_order_transfer_function - expected_second_order_transfer_function) == 0
assert sp.simplify(dc_gain - 1) == 0
assert sp.simplify(step_output - concrete_transfer_function * step_transform) == 0

print()
print("All Laplace intuition checks passed.")
