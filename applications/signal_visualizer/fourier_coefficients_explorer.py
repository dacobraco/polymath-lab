import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

t = sp.symbols("t", real=True)
symbolic_T = 2 * sp.pi
symbolic_omega0 = 2 * sp.pi / symbolic_T

symbolic_an = []
symbolic_bn = []

symbolic_a0 = sp.simplify(2 / symbolic_T * (sp.integrate(-1, (t, -sp.pi, 0)) + sp.integrate(1, (t, 0, sp.pi))))

for n in range(1, 11):
    an = sp.simplify(2 / symbolic_T * (sp.integrate(-sp.cos(n * symbolic_omega0 * t), (t, -sp.pi, 0)) + sp.integrate(sp.cos(n * symbolic_omega0 * t), (t, 0, sp.pi))))
    bn = sp.simplify(2 / symbolic_T * (sp.integrate(-sp.sin(n * symbolic_omega0 * t), (t, -sp.pi, 0)) + sp.integrate(sp.sin(n * symbolic_omega0 * t), (t, 0, sp.pi))))
    symbolic_an.append(an)
    symbolic_bn.append(bn)

t_numeric = np.linspace(-np.pi, np.pi, 10001)
x_numeric = np.sign(t_numeric)
T_numeric = 2 * np.pi
omega0_numeric = 2 * np.pi / T_numeric

numerical_a0 = 2 / T_numeric * np.trapezoid(x_numeric, t_numeric)

numerical_an = []
numerical_bn = []

for n in range(1, 11):
    an = 2 / T_numeric * np.trapezoid(x_numeric * np.cos(n * omega0_numeric * t_numeric), t_numeric)
    bn = 2 / T_numeric * np.trapezoid(x_numeric * np.sin(n * omega0_numeric * t_numeric), t_numeric)
    numerical_an.append(an)
    numerical_bn.append(bn)

absolute_errors = []

print("n | symbolic_bn | numerical_bn | absolute_error")

for n, (symbolic_value, numerical_value) in enumerate(zip(symbolic_bn, numerical_bn), start=1):
    symbolic_decimal = float(sp.N(symbolic_value))
    error = abs(symbolic_decimal - numerical_value)
    absolute_errors.append(error)

    print(
        f"{n} | {symbolic_value} | "
        f"{numerical_value:.8f} | {error:.3e}"
        )

print("a0 is approximately zero:", np.isclose(numerical_a0, 0, atol=10**-6, rtol=0))
print("an is approximately zero:", np.allclose(numerical_an, 0, atol=10**-6, rtol=0))
print("b2, b4, b6... are approximately zero:", np.allclose(numerical_bn[1::2], 0, atol=10**-6, rtol=0))

expected = []

for n in range(1, 10, 2):
    value = 4 / (n * np.pi)
    expected.append(value)

print("b1, b3, b5... are the same as expected:", np.allclose(numerical_bn[::2], expected, atol=10**-6, rtol=0))

symbolic_bn_decimal = [float(sp.N(value)) for value in symbolic_bn]

n_values = np.arange(1, 11)

fig, ax = plt.subplots(figsize=(9, 5))

ax.stem(
    n_values,
    symbolic_bn_decimal,
    linefmt="C0-",
    markerfmt="C0o",
    basefmt=" ",
    label="Symbolic"
)

ax.stem(
    n_values,
    numerical_bn,
    linefmt="C1--",
    markerfmt="C1x",
    basefmt=" ",
    label="Numerical"
)

ax.set_title("Fourier Sine Coefficients: Symbolic vs Numerical")
ax.set_xlabel("Harmonic Number n")
ax.set_ylabel("Coefficient b_n")
ax.set_xticks(n_values)
ax.grid(True, alpha=0.3)
ax.legend()

plt.tight_layout()
plt.show()
