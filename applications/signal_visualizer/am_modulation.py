import numpy as np
import matplotlib.pyplot as plt

fs = 100_000
duration = 0.02
fm = 200
fc = 5000
mu = 1.2

time = np.arange(0, duration, 1/fs)

message = np.cos(2 * np.pi * fm * time)
carrier = np.cos(2 * np.pi * fc * time)
am_signal = (1 + mu * message) * carrier

fourier = np.fft.rfft(am_signal)
frequencies = np.fft.rfftfreq(len(time), d=1/fs)
magnitudes = np.abs(fourier)

rectified = np.abs(am_signal)

period_samples = int(fs / fc)
kernel = np.ones(period_samples) / period_samples

envelope = np.convolve(rectified, kernel, mode="same")

demodulated = envelope - np.mean(envelope)
demodulated = demodulated / np.max(np.abs(demodulated))

plt.figure()
plt.plot(time, message, label="Message signal")
plt.plot(time, am_signal, label="AM signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(frequencies, magnitudes)
plt.xlim(4000, 6000)
plt.xlabel("Frequency [Hz]")
plt.ylabel("Magnitude")
plt.grid(True)

plt.figure()
plt.plot(time, message, label="Message signal")
plt.plot(time, envelope, label="Envelope")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.figure()
plt.plot(time, message, label="Original message")
plt.plot(time, demodulated, label="Demodulated signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()

plt.show()
