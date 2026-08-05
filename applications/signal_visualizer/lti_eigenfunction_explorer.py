import numpy as np
import matplotlib.pyplot as plt

f = 2  # Hz
tau = 0.125  # s
t = np.linspace(0, 1, 1000)
omega = 2 * np.pi * f

input_signal = np.exp(1j * omega * t)  # x(t)
output_signal = np.exp(1j * omega * (t - tau))  # y(t)

system_factor = output_signal / input_signal  # H(jω)
constant_factor = np.allclose(system_factor, system_factor[0])
theoretical_factor = np.exp(-1j * omega * tau)  # Theoretical H(jω)
matches_theory = np.allclose(system_factor, theoretical_factor)

print(f"System factor: {system_factor[0]}")
print(f"Theoretical factor: {theoretical_factor}")
print(f"Constant factor: {constant_factor}")
print(f"Matches theory: {matches_theory}")

plt.plot(t, input_signal.real, label="Input signal")
plt.plot(t, output_signal.real, label="Output signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("LTI Eigenfunction: Input and Delayed Output")
plt.legend()
plt.grid(True)
plt.show()
