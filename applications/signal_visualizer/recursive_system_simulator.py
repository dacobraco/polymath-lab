import numpy as np
import matplotlib.pyplot as plt


def simulate_recursive_system(input_values, coefficient, initial_output=0.0):
    output_values = []

    previous_output = initial_output

    for input_value in input_values:
        current_output = coefficient * previous_output + input_value

        output_values.append(current_output)
        previous_output = current_output

    return np.array(output_values)


def classify_stability(coefficient):
    if abs(coefficient) < 1:
        return "Stable"

    if abs(coefficient) == 1:
        return "Marginal"

    return "Unstable"


input_values = np.array([0, 0, 2, 2, 0, 0, 0, 0, 0, 0], dtype=float)

coefficients = [0.2, 0.5, 0.9, 1.0, 1.1]

for coefficient in coefficients:
    output_values = simulate_recursive_system(input_values, coefficient)

    print("Coefficient:", coefficient)
    print("Stability:", classify_stability(coefficient))
    print("Output:", output_values)
    print()


impulse_input = np.array([1, 0, 0, 0, 0, 0, 0, 0], dtype=float)

impulse_output = simulate_recursive_system(impulse_input, 0.5)

expected_impulse = 0.5 ** np.arange(len(impulse_input))

print("Impulse input:", impulse_input)
print("Impulse response:", impulse_output)
print("Expected impulse response:", expected_impulse)

assert np.allclose(impulse_output, expected_impulse)

print("Impulse-response check: PASSED")


figure, axes = plt.subplots(2, 1, figsize=(10, 8))

for coefficient in coefficients:
    output_values = simulate_recursive_system(input_values, coefficient)
    axes[0].plot(output_values, marker="o", label=f"a = {coefficient}")

axes[0].set_title("Recursive System Response")
axes[0].set_xlabel("Sample n")
axes[0].set_ylabel("y[n]")
axes[0].grid(True)
axes[0].legend()

axes[1].stem(impulse_output)
axes[1].set_title("Impulse Response for a = 0.5")
axes[1].set_xlabel("Sample n")
axes[1].set_ylabel("h[n]")
axes[1].grid(True)

plt.tight_layout()
plt.show()
