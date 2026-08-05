import numpy as np
import matplotlib.pyplot as plt

f = 2  # Hz
t = np.linspace(0, 1, 1000)
tau = 0.125  # s

original_signal = np.exp(1j * 2 * np.pi * f * t).real
delayed_signal = np.exp(1j * 2 * np.pi * f * (t - tau)).real

plt.plot(t, original_signal, label="Original Signal (real)")
plt.plot(t, delayed_signal, label="Delayed Signal (real)")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.title("Signal Delay and Phase Shift")
plt.legend()
plt.grid(True)
plt.show()
