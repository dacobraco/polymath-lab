import control
import matplotlib.pyplot as plt

plant = control.tf([2], [5, 1])
Kp = 2
regulator = 2
series = regulator * plant
closed_loop = control.feedback(series, 1)
time, response = control.step_response(closed_loop)

Ki = 2
s = control.tf([1, 0], [1])
regulator_ki = Kp + Ki / s
series_ki = regulator_ki * plant
closed_loop_ki = control.feedback(series_ki, 1)
time_ki, response_ki = control.step_response(closed_loop_ki)

Kd = [0, 0.5, 1, 2]
for kd in Kd:
    s = control.tf([1, 0], [1])
    regulator_kd = Kp + Ki / s + kd * s
    series_kd = regulator_kd * plant
    closed_loop_kd = control.feedback(series_kd, 1)
    time_kd, response_kd = control.step_response(closed_loop_kd)
    plt.plot(time_kd, response_kd, label=f"kd = {kd}")
    info = control.step_info(closed_loop_kd)
    print("Kd =", kd, "Overshoot:", info["Overshoot"], "SettlingTime:", info["SettlingTime"])

plt.xlabel("Time [s]")
plt.ylabel("Response")
plt.axhline(1, linestyle="--")
plt.grid(True)
plt.legend()
plt.show()
