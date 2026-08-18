import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 1, 101)
f = 2
x = np.sin(2 * np.pi * f * t)

plt.plot(t, x)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("2 Hz Sine Wave")
plt.grid(True)
plt.tight_layout()
plt.show()
