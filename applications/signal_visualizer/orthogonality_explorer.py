import numpy as np
import matplotlib.pyplot as plt

def inner_product(x, y, dt):
    total = 0
    for i in range(len(x)):
        total += x[i] * y[i]
    return total * dt

def projection_coefficient(signal, basis, dt):
    c = inner_product(signal, basis, dt) / inner_product(basis, basis, dt)
    return c

T = 1
frequency = 1 / T
omega_0 = 2 * np.pi * frequency

t = np.linspace(0, T, 2000, endpoint=False)
dt = t[1] - t[0]

sin1 = np.sin(omega_0 * t)
cos1 = np.cos(omega_0 * t)
sin2 = np.sin(2 * omega_0 * t)
cos2 = np.cos(2 * omega_0 * t)

x = 3 * sin1 + 0.5 * cos2

c_sin1 = projection_coefficient(x, sin1, dt)
c_cos1 = projection_coefficient(x, cos1, dt)
c_sin2 = projection_coefficient(x, sin2, dt)
c_cos2 = projection_coefficient(x, cos2, dt)

x_reconstructed = c_sin1 * sin1 + c_cos1 * cos1 + c_sin2 * sin2 + c_cos2 * cos2

fig, axes = plt.subplots(3, 1, figsize=(9, 8), sharex=True)
fig.suptitle("Orthogonality and Signal Projection")
axes[0].plot(t, sin1, label="Sine")
axes[0].plot(t, cos1, label="Cosine")
axes[0].set_title("First Harmonic Basis")
axes[1].plot(t, sin2, label="Sine")
axes[1].plot(t, cos2, label="Cosine")
axes[1].set_title("Second Harmonic Basis")
axes[2].plot(t, x, label="x")
axes[2].plot(t, x_reconstructed, label="x_reconstructed", linestyle="--")
axes[2].set_xlabel("Time [s]")
for i in range(3):
    axes[i].set_ylabel("Amplitude")
    axes[i].grid(True)
    axes[i].legend()

plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()

print(f"sin1 coefficient: {c_sin1}")
print(f"cos1 coefficient: {c_cos1}")
print(f"sin2 coefficient: {c_sin2}")
print(f"cos2 coefficient: {c_cos2}")
print(f"Reconstruction matches: {np.allclose(x, x_reconstructed)}")
