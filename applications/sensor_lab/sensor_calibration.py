import numpy as np
import matplotlib.pyplot as plt

true_temperature = 25.0
rng = np.random.default_rng(42)
noise = rng.normal(0, 0.6, 1000)

T = np.array([10.0, 30.0])
M = np.array([13.0, 37.0])
a, b = np.polyfit(T, M, 1)

readings = a * true_temperature + b + noise
results = (readings - b) / a

print("N\t\tMean")
for N in [5, 20, 200, 1000]:
    print(f"{N}\t\t{np.mean(results[:N])}")

plt.plot(results[:100], label="Calibrated")
plt.xlabel("Index")
plt.ylabel("Temperature")
plt.axhline(true_temperature, label="True Temperature", color="red")
plt.grid(True)
plt.legend()
plt.show()
