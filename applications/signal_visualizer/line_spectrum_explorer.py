import numpy as np
import matplotlib.pyplot as plt

n = np.arange(1, 11)

an = np.zeros_like(n)
bn = 2 * ((-1) ** (n + 1)) / (n * np.pi)

amplitude_n = np.sqrt(an ** 2 + bn ** 2)
phase_n = np.degrees(np.atan2(-bn, an))

print(f"n: {n}\nbn: {bn}\nAn: {amplitude_n}\nPhase: {phase_n}")

fig, axes = plt.subplots(2, 1, sharex=True, figsize=(8, 7))
axes[0].stem(n, amplitude_n)
axes[0].set_title("Sawtooth Amplitude Spectrum")
axes[0].set_ylabel("Amplitude A_n")
axes[1].stem(n, phase_n)
axes[1].set_title("Sawtooth Phase Spectrum")
axes[1].set_ylabel("Phase [deg]")
axes[1].set_xlabel("Harmonic Number n")
axes[1].set_xlim(0.5, 10.5)
axes[1].set_xticks(n)
axes[1].set_yticks([-90, 0, 90])

for ax in axes:
    ax.grid(True)

plt.tight_layout()
plt.show()
