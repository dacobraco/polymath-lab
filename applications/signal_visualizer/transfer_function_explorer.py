import control
import matplotlib.pyplot as plt

numerator = [2]
denominator = [1, 1]
transfer_function = control.tf(numerator, denominator)
time, response = control.step_response(transfer_function)

transfer_function_2 = control.tf([2], [5, 1])
time_2, response_2 = control.step_response(transfer_function_2)

control_tf = control.tf([4], [1])
transfer_series = control.series(control_tf, transfer_function_2)
print(transfer_series)
series_time, series_response = control.step_response(transfer_series)

closed_loop = control.feedback(transfer_series, 1)
print(closed_loop)
closed_time, closed_response = control.step_response(closed_loop)

plt.plot(time, response, label="tau = 1")
plt.plot(time_2, response_2, label="tau = 5")
plt.plot(series_time, series_response, label="Series")
plt.plot(closed_time, closed_response, label="Closed response")
plt.xlabel("Time [s]")
plt.ylabel("Response")
plt.grid(True)
plt.legend()
plt.show()
