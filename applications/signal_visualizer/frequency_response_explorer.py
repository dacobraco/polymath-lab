import numpy as np
import matplotlib.pyplot as plt

tau = 0.125  # s
frequencies = np.linspace(0, 10, 1000)
omega = 2 * np.pi * frequencies

H = np.exp(-1j * omega * tau)

magnitude = np.abs(H)
phase_wrapped = np.degrees(np.angle(H))
phase_unwrapped = np.degrees(np.unwrap(np.angle(H)))

print("Magnitude constant:", np.allclose(magnitude, 1))
print(f"Final unwrapped phase [deg]: {phase_unwrapped[-1]}")
print(f"Final wrapped phase [deg]: {phase_wrapped[-1]}")

fig, axes = plt.subplots(3, 1, sharex=True)
axes[0].plot(frequencies, magnitude)
axes[1].plot(frequencies, phase_wrapped)
axes[2].plot(frequencies, phase_unwrapped)

axes[0].set_ylabel("Magnitude")
axes[1].set_ylabel("Wrapped phase [deg]")
axes[2].set_ylabel("Unwrapped phase [deg]")
axes[2].set_xlabel("Frequency [Hz]")
axes[0].set_title("Frequency Response of a Pure Delay")

for ax in axes:
    ax.grid(True)

plt.tight_layout()
plt.show()
