import numpy as np
import matplotlib.pyplot as plt


time_constant = 1.0
sample_interval = 0.2
duration = 5.0
step_input = 1.0

continuous_pole = -1 / time_constant
continuous_time = np.linspace(0, duration, 1001)
continuous_response = step_input * (1 - np.exp(-continuous_time / time_constant))
number_of_samples = int(duration / sample_interval) + 1
sample_time = np.arange(number_of_samples) * sample_interval
discrete_pole = np.exp(continuous_pole * sample_interval)
discrete_response = np.zeros(number_of_samples)

for sample_index in range(1, number_of_samples):
    previous_output = discrete_response[sample_index - 1]

    discrete_response[sample_index] = (discrete_pole * previous_output + (1 - discrete_pole) * step_input)

exact_response_at_samples = step_input * (1 - np.exp(-sample_time / time_constant))
absolute_error = np.abs(discrete_response - exact_response_at_samples)
maximum_error = np.max(absolute_error)

print("Time constant:", time_constant, "s")
print("Sample interval:", sample_interval, "s")
print("Continuous pole:", continuous_pole)
print("Discrete pole:", discrete_pole)
print("Previous-output weight:", discrete_pole)
print("New-input weight:", 1 - discrete_pole)
print("Number of samples:", number_of_samples)
print("Maximum error:", maximum_error)

plt.figure(figsize=(10, 6))
plt.plot(continuous_time, continuous_response, label="Continuous response", linewidth=2)
plt.stem(
    sample_time,
    discrete_response,
    linefmt="C1-",
    markerfmt="C1o",
    basefmt=" ",
    label="Discrete response"
)

plt.xlabel("Time [s]")
plt.ylabel("Output")
plt.title("Continuous and Discrete First-Order System")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
