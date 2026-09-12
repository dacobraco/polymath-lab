import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

numerator = [9]
denominator = [1, 2, 10]

system = signal.TransferFunction(numerator, denominator)

print("SciPy transfer function:")
print(system)

print("Poles:", system.poles)
print("Zeros:", system.zeros)

time_values = np.linspace(0, 8, 801)

step_time, step_response = signal.step(system, T=time_values)
impulse_time, impulse_response = signal.impulse(system, T=time_values)

print("\nControlled time grid")
print("Number of points:", len(time_values))
print("Start time:", time_values[0])
print("End time:", time_values[-1])

print("\nSelected step-response values")
print("t = 0 s:", step_response[0])
print("t = 1 s:", step_response[100])
print("t = 2 s:", step_response[200])
print("t = 8 s:", step_response[-1])

print("\nSelected impulse-response values")
print("t = 0 s:", impulse_response[0])
print("t = 1 s:", impulse_response[100])
print("t = 2 s:", impulse_response[200])
print("t = 8 s:", impulse_response[-1])

figure, axes = plt.subplots(2, 1, figsize=(10, 8))

axes[0].plot(step_time, step_response)
axes[0].axhline(0.9, linestyle="--", label="DC gain = 0.9")
axes[0].set_title("SciPy Step Response")
axes[0].set_xlabel("Time [s]")
axes[0].set_ylabel("y(t)")
axes[0].grid(True)
axes[0].legend()

axes[1].plot(impulse_time, impulse_response)
axes[1].set_title("SciPy Impulse Response")
axes[1].set_xlabel("Time [s]")
axes[1].set_ylabel("h(t)")
axes[1].grid(True)

plt.tight_layout()
plt.show()
