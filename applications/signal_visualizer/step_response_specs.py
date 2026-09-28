import control
import matplotlib.pyplot as plt

system_1 = control.tf([25], [1, 2, 25])
system_2 = control.tf([25], [1, 4, 25])
system_3 = control.tf([25], [1, 8, 25])
system_4 = control.tf([25], [1, 7, 25])
system_5 = control.tf([25], [1, 10, 25])

time_1, response_1 = control.step_response(system_1)
time_2, response_2 = control.step_response(system_2)
time_3, response_3 = control.step_response(system_3)
time_4, response_4 = control.step_response(system_4)
time_5, response_5 = control.step_response(system_5)

info_1 = control.step_info(system_1)
info_2 = control.step_info(system_2)
info_3 = control.step_info(system_3)
info_4 = control.step_info(system_4)
info_5 = control.step_info(system_5)

print("zeta = 0.2:", info_1)
print("zeta = 0.4:", info_2)
print("zeta = 0.8:", info_3)
print("zeta = 0.7:", info_4)
print("zeta = 1.0:", info_5)

plt.plot(time_1, response_1, label="zeta = 0.2")
plt.plot(time_2, response_2, label="zeta = 0.4")
plt.plot(time_3, response_3, label="zeta = 0.8")
plt.plot(time_4, response_4, label="zeta = 0.7")
plt.plot(time_5, response_5, label="zeta = 1.0")

plt.axhline(1)
plt.xlabel("Time [s]")
plt.ylabel("Response")
plt.grid(True)
plt.legend()
plt.show()
