import math
import matplotlib.pyplot as plt

P_T = 20  # dBm
G_T = 2  # dB
G_R = 2  # dB
d = 1  # km
f = 900  # MHz
sensitivity = -90  # dBm

fspl = 32.44 + 20 * math.log10(d) + 20 * math.log10(f)
P_R = P_T + G_T + G_R - fspl
margin = P_R - sensitivity
print("FSPL:", fspl)
print("Received power:", P_R)
print("Link margin:", margin)

fig, ax = plt.subplots(figsize=(10, 4))

ax.add_patch(plt.Rectangle((0.5, 1), 2, 1, fill=False))
ax.add_patch(plt.Rectangle((4, 1), 2, 1, fill=False))
ax.add_patch(plt.Rectangle((7.5, 1), 2, 1, fill=False))

ax.text(1.5, 1.5, f"Transmitter\nP_T = {P_T} dBm", ha="center", va="center")
ax.text(5, 1.5, f"Channel\nFSPL = {fspl:.2f} dB", ha="center", va="center")
ax.text(8.5, 1.5, f"Receiver\nP_R = {P_R:.2f} dBm", ha="center", va="center")

ax.annotate("", xy=(4, 1.5), xytext=(2.5, 1.5), arrowprops=dict(arrowstyle="->"))
ax.annotate("", xy=(7.5, 1.5), xytext=(6, 1.5), arrowprops=dict(arrowstyle="->"))

ax.text(8.5, 0.6, f"Link margin = {margin:.2f} dB", ha="center")

ax.set_xlim(0, 10)
ax.set_ylim(0, 3)
ax.axis("off")
ax.set_title("Communication Link Budget")

plt.show()
