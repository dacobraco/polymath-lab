import numpy as np
from scipy.integrate import simpson
from fourier_properties import numerical_fourier_transform

t = np.linspace(-5, 5, 5001)
x = np.exp(-np.pi * t**2)

energy_time = simpson(np.abs(x**2), x=t)

print("Time-domain energy:", energy_time)

frequencies = np.linspace(-5, 5, 501)

X = numerical_fourier_transform(t, x, frequencies)

energy_frequency = simpson(np.abs(X)**2, x=frequencies)

parseval_error = np.abs(energy_time - energy_frequency)

print("Frequency-domain energy:", energy_frequency)
print("Parseval error:", parseval_error)
