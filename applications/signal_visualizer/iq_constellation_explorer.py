import numpy as np
import matplotlib.pyplot as plt

I = np.array([1, -1, -1, 1])
Q = np.array([1, 1, -1, -1])
n = 1000
noise_std = 0.8

noise1 = np.random.normal(0, noise_std, n)
noise2 = np.random.normal(0, noise_std, n)
noise = noise1 + 1j * noise2

z = I + 1j*Q
sent = np.random.choice(z, size=n)
received = sent + noise

I_received = np.where(received.real >= 0, 1, -1)
Q_received = np.where(received.imag >= 0, 1, -1)

detected = I_received + 1j * Q_received
errors = sent != detected
ser = np.mean(errors)
print("SER:", ser*100, "%")

plt.scatter(received.real, received.imag)
plt.xlabel("In-phase (I)")
plt.ylabel("Quadrature (Q)")
plt.axis("equal")
plt.grid(True)
plt.show()
