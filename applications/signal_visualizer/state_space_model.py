import numpy as np
import matplotlib.pyplot as plt
import control

A = np.array([[0, 1], [-5, -2]])
B = np.array([[0], [1]])
C = np.array([[1, 0], [0, 1]])
D = np.array([[0], [0]])

system = control.ss(A, B, C, D)

x0 = np.array([1, 0])
time = np.linspace(0, 10, 500)
response = control.initial_response(system, time, X0=x0)
poles = control.poles(system)
step_result = control.step_response(system, time)

u = np.sin(2*time)
u_5 = np.sin(5*time)

transfer_system = control.ss2tf(system)
forced_2 = control.forced_response(system, time, u)
forced_5 = control.forced_response(system, time, u_5)

plt.plot(response.time, response.outputs[0], label="Position")
plt.plot(response.time, response.outputs[1], label="Velocity")
plt.plot(step_result.time, step_result.outputs[0, 0], label="Step response position")
plt.plot(step_result.time, step_result.outputs[1, 0], label="Step response velocity")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(forced_2.time, forced_2.outputs[0], label="Position")
plt.plot(forced_2.time, forced_2.outputs[1], label="Velocity")
plt.plot(time, u, label="Input")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(forced_2.time, forced_2.outputs[0], label="Position ω = 2")
plt.plot(forced_5.time, forced_5.outputs[0], label="Position ω = 5")
plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.grid(True)
plt.legend()
plt.show()
