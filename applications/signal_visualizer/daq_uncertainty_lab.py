import numpy as np
import matplotlib.pyplot as plt

T_ref = np.array([10., 20., 30., 40., 50.])
M = np.array([11.2, 21.8, 32.9, 43.1, 54.0])

a, b = np.polyfit(T_ref, M, 1)
M_fit = a*T_ref + b
residuals = M - M_fit
s_r = np.sqrt(np.sum(residuals**2) / (len(T_ref) - 2))
print("Residual standard deviation:", s_r, "°C")

print(residuals)

M_new = 38.0
T_est = (M_new - b) / a
s_T = s_r / abs(a)

print("Estimated temperature:", T_est, "°C")
print("Residual standard deviation:", s_r, "°C")
print("Temperature uncertainty component:", s_T, "°C")

u_ref = 0.05
u_combined = np.sqrt(s_T**2 + u_ref**2)

print("Combined uncertainty:", u_combined, "°C")

plt.figure()
plt.plot(T_ref, M_fit, label="Calibration fit")
plt.scatter(T_ref, M, label="Measurements")
plt.xlabel("Referent temperature")
plt.ylabel("Measured temperature")
plt.grid(True)

plt.figure()
plt.plot(T_ref, residuals)
plt.axhline(0, color="red", linestyle="--")
plt.show()
