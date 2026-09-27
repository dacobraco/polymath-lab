import matplotlib.pyplot as plt

reference = 22.0
temperature = 18.0
kp = 0.5
ki = 0.05
outside_temperature = 5.0
heat_loss_coefficient = 0.05
integral = 0.0

temperature_history = []

for _ in range(50):
    error = reference - temperature
    integral += error
    control = kp * error + ki * integral
    heat_loss = heat_loss_coefficient * (temperature - outside_temperature)
    temperature_change = control - heat_loss

    temperature += temperature_change
    temperature_history.append(temperature)

print("Temperature:", temperature)

plt.plot(temperature_history, label="Temperature")
plt.axhline(reference, linestyle="--", label="Reference")
plt.xlabel("Iteration")
plt.ylabel("Temperature (°C)")
plt.title("PI Feedback Control Response")
plt.legend()
plt.grid()
plt.show()
