import numpy as np
import matplotlib.pyplot as plt

R = 10_000
C = 100e-9
frequencies = np.logspace(0, 5, 501)
f_ltspice = 159.34839
fc = 1 / (2*np.pi*R*C)

H = 1 / (1 + 1j*2*np.pi*frequencies*R*C)
amplitude_db = 20*np.log10(np.abs(H))
phase = np.angle(H, deg=True)

H_ltspice = 1 / (1 + 1j*2*np.pi*f_ltspice*R*C)
amplitude_ltspice = 20*np.log10(np.abs(H_ltspice))
phase_ltspice = np.angle(H_ltspice, deg=True)

print(H_ltspice)
print(amplitude_ltspice)
print(phase_ltspice)

plt.semilogx(frequencies, amplitude_db, label="Amplitude")
plt.xlabel("Frequency [Hz]")
plt.ylabel("Gain [dB]")
plt.axvline(fc, color="red")
plt.grid(True)
plt.legend()
plt.show()
