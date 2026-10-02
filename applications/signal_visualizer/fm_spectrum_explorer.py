import numpy as np
import matplotlib.pyplot as plt

fs = 100_000
duration = 0.1
fm = 200
fc = 5000
delta_f = 200
t = np.arange(0, duration, 1/fs)
beta = delta_f / fm
kp = 1

message = np.cos(2*np.pi*fm*t)
carrier = np.cos(2*np.pi*fc*t)
instantaneous_frequency = fc + delta_f*message
phase = 2*np.pi*fc*t + beta*np.sin(2*np.pi*fm*t)

fm_signal = np.cos(phase)
pm_signal = np.cos(2*np.pi*fc*t + kp*message)
pm_frequency = fc + kp/(2*np.pi) * np.gradient(message, 1/fs)

fm_rfft = np.fft.rfft(fm_signal)
fm_frequencies = np.fft.rfftfreq(len(fm_signal), d=1/fs)
fm_amplitude = np.abs(fm_rfft) * 2 / len(fm_signal)

plt.plot(t, carrier, label="Carrier")
plt.plot(t, fm_signal, label="FM signal")
plt.xlim(0, 0.003)
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(fm_frequencies, fm_amplitude)
plt.xlim(2000, 8000)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Amplitude")
plt.grid(True)

plt.figure()
plt.plot(t, instantaneous_frequency, label="FM frequency")
plt.plot(t, pm_frequency, label="PM frequency")
plt.xlim(0, 0.01)
plt.xlabel("Time[s]")
plt.ylabel("Frequency [Hz]")
plt.grid(True)
plt.legend()
plt.show()
