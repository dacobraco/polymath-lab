import numpy as np
import matplotlib.pyplot as plt

n = np.arange(-5, 11)

def unit_impulse(n, position):
    impulse = np.zeros(len(n))
    index = np.argmin(np.abs(n - position))
    impulse[index] = 1
    return impulse

delta_n = unit_impulse(n, 0)
delta_n_minus_1 = unit_impulse(n, 1)

h1 = 2 * delta_n
h2 = delta_n_minus_1
h3 = delta_n + 0.5 * delta_n_minus_1

print("h1[n]:", h1)
print("h2[n]:", h2)
print("h3[n]:", h3)

fig, axes = plt.subplots(4, 1, sharex=True)
axes[0].stem(n, delta_n)
axes[1].stem(n, h1)
axes[2].stem(n, h2)
axes[3].stem(n, h3)
axes[3].set_xlabel("n")
axes[0].set_ylabel("δ[n]")
axes[1].set_ylabel("h1[n]")
axes[2].set_ylabel("h2[n]")
axes[3].set_ylabel("h3[n]")
axes[0].set_title("Impulse response")

for ax in axes:
    ax.grid(True)

plt.tight_layout()
plt.show()
