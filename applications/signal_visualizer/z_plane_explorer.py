import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

def analyze_causal_system(feedback_coefficient):
    pole = feedback_coefficient
    zero = 0
    roc_radius = abs(pole)

    if roc_radius < 1:
        stability = "Stable"
    elif roc_radius == 1:
        stability = "Boundary - not BIBO stable"
    else:
        stability = "Unstable"

    return pole, zero, roc_radius, stability


systems = {
    "Fast decay": 0.5,
    "Slow decay": 0.9,
    "Boundary": 1.0,
    "Growing response": 1.1
}


for system_name, feedback_coefficient in systems.items():
    pole, zero, roc_radius, stability = analyze_causal_system(feedback_coefficient)

    print()
    print("System:", system_name)
    print("Feedback coefficient:", feedback_coefficient)
    print("Pole:", pole)
    print("Zero:", zero)
    print("Causal ROC: |z| >", roc_radius)
    print("Stability:", stability)

angles = np.linspace(0, 2 * np.pi, 500)

unit_circle_x = np.cos(angles)
unit_circle_y = np.sin(angles)

figure, axes = plt.subplots(2, 2, figsize=(11, 9))
axes = axes.flatten()

for axis, (system_name, feedback_coefficient) in zip(axes, systems.items()):
    pole, zero, roc_radius, stability = analyze_causal_system(feedback_coefficient)

    axis.set_facecolor("#dff3df")

    non_roc_area = Circle(
        (0, 0),
        roc_radius,
        facecolor="white",
        edgecolor="green",
        linestyle=":",
        linewidth=2,
        zorder=0
    )

    axis.add_patch(non_roc_area)

    axis.text(
        -1.32,
        1.25,
        f"ROC: |z| > {roc_radius}",
        color="green",
        fontsize=9
    )

    axis.plot(unit_circle_x, unit_circle_y, "b--", label="Unit circle")
    axis.scatter(zero, 0, facecolors="none", edgecolors="blue", s=100, label="Zero")
    axis.scatter(pole, 0, color="red", marker="x", s=100, label="Pole")

    axis.axhline(0, color="black", linewidth=0.8)
    axis.axvline(0, color="black", linewidth=0.8)

    axis.set_xlim(-1.4, 1.4)
    axis.set_ylim(-1.4, 1.4)
    axis.set_aspect("equal")
    axis.set_xlabel("Real part")
    axis.set_ylabel("Imaginary part")
    axis.set_title(f"{system_name}: a = {feedback_coefficient}\n{stability}")
    axis.grid(True)
    axis.legend()

figure.suptitle("Poles and the Unit Circle in the Z-plane")
sample_indices = np.arange(0, 21)

response_figure, response_axes = plt.subplots(2, 2, figsize=(11, 8))
response_axes = response_axes.flatten()

for axis, (system_name, feedback_coefficient) in zip(response_axes, systems.items()):
    impulse_response = feedback_coefficient ** sample_indices

    axis.stem(sample_indices, impulse_response)
    axis.axhline(0, color="black", linewidth=0.8)
    axis.set_xlabel("Sample n")
    axis.set_ylabel("h[n]")
    axis.set_title(f"{system_name}: a = {feedback_coefficient}")
    axis.grid(True)

response_figure.suptitle("Impulse Responses: h[n] = a^n")
negative_coefficient = -0.9
negative_response = negative_coefficient ** sample_indices

negative_figure, negative_axes = plt.subplots(1, 2, figsize=(12, 5))

negative_axes[0].set_facecolor("#dff3df")

non_roc_area = Circle(
    (0, 0),
    abs(negative_coefficient),
    facecolor="white",
    edgecolor="green",
    linestyle=":",
    linewidth=2,
    zorder=0
)

negative_axes[0].add_patch(non_roc_area)
negative_axes[0].plot(unit_circle_x, unit_circle_y, "b--", label="Unit circle")
negative_axes[0].scatter(0, 0, facecolors="none", edgecolors="blue", s=100)
negative_axes[0].scatter(negative_coefficient, 0, color="red", marker="x", s=100)
negative_axes[0].axhline(0, color="black", linewidth=0.8)
negative_axes[0].axvline(0, color="black", linewidth=0.8)
negative_axes[0].set_xlim(-1.4, 1.4)
negative_axes[0].set_ylim(-1.4, 1.4)
negative_axes[0].set_aspect("equal")
negative_axes[0].set_xlabel("Real part")
negative_axes[0].set_ylabel("Imaginary part")
negative_axes[0].set_title("Stable pole at z = -0.9")
negative_axes[0].grid(True)
negative_axes[0].legend()

negative_axes[1].stem(sample_indices, negative_response)
negative_axes[1].axhline(0, color="black", linewidth=0.8)
negative_axes[1].set_xlabel("Sample n")
negative_axes[1].set_ylabel("h[n]")
negative_axes[1].set_title("Impulse response: h[n] = (-0.9)^n")
negative_axes[1].grid(True)

negative_figure.suptitle("A Negative Pole Produces Alternating Samples")
pole_radius = 0.9
pole_angle = np.pi / 4

upper_pole = pole_radius * np.exp(1j * pole_angle)
lower_pole = np.conjugate(upper_pole)

oscillatory_response = pole_radius ** sample_indices * np.cos(
    pole_angle * sample_indices
)

complex_figure, complex_axes = plt.subplots(1, 2, figsize=(12, 5))

complex_axes[0].set_facecolor("#dff3df")

non_roc_area = Circle(
    (0, 0),
    pole_radius,
    facecolor="white",
    edgecolor="green",
    linestyle=":",
    linewidth=2,
    zorder=0
)

complex_axes[0].add_patch(non_roc_area)
complex_axes[0].plot(unit_circle_x, unit_circle_y, "b--", label="Unit circle")

complex_axes[0].scatter(
    [upper_pole.real, lower_pole.real],
    [upper_pole.imag, lower_pole.imag],
    color="red",
    marker="x",
    s=100,
    label="Poles"
)

complex_axes[0].axhline(0, color="black", linewidth=0.8)
complex_axes[0].axvline(0, color="black", linewidth=0.8)
complex_axes[0].set_xlim(-1.4, 1.4)
complex_axes[0].set_ylim(-1.4, 1.4)
complex_axes[0].set_aspect("equal")
complex_axes[0].set_xlabel("Real part")
complex_axes[0].set_ylabel("Imaginary part")
complex_axes[0].set_title("Complex poles: radius 0.9, angle pi/4")
complex_axes[0].grid(True)
complex_axes[0].legend()

complex_axes[1].stem(sample_indices, oscillatory_response)
complex_axes[1].axhline(0, color="black", linewidth=0.8)
complex_axes[1].set_xlabel("Sample n")
complex_axes[1].set_ylabel("h[n]")
complex_axes[1].set_title("Decaying oscillation")
complex_axes[1].grid(True)

complex_figure.suptitle("Pole Radius and Angle")
plt.tight_layout()
plt.show()

print()
print("Upper complex pole:", upper_pole)
print("Lower complex pole:", lower_pole)
print("Pole radius:", abs(upper_pole))
print("Pole angle:", np.angle(upper_pole))
