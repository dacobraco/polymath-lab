import numpy as np
import matplotlib.pyplot as plt

rng = np.random.default_rng(81)
ideal_voltage = 1.0
sample_count = 10_000
sample_sizes = [10, 100, 1000, 10000]

noise = rng.uniform(-1, 1, sample_count)
measured_voltage = ideal_voltage + noise

for size in sample_sizes:
    selected_measurements = measured_voltage[:size]
    event_count = np.sum(selected_measurements > 1.6)
    total_count = len(selected_measurements)
    estimated_probability = event_count / total_count
    print(f"Event count: {event_count}\t Total: {total_count}\t Estimated probability: {estimated_probability}")

events = measured_voltage > 1.6
cumulative_events = np.cumsum(events)
measurement_numbers = np.arange(1, sample_count + 1)
cumulative_probability = cumulative_events / measurement_numbers
print(cumulative_probability[:5])
print(cumulative_probability[-1])
print(len(cumulative_probability))

plt.plot(measurement_numbers, cumulative_probability, label="Estimated probability")
plt.axhline(0.2, color="red", linestyle="--", label="Theoretical probability")
plt.xlabel("Measurements")
plt.ylabel("Probability")
plt.title("Probability convergence")
plt.grid(True)
plt.legend()

assert len(measured_voltage) == sample_count
assert cumulative_events[-1] == 1988
assert np.isclose(cumulative_probability[-1], 0.1988)

print("All validation checks passed.")

plt.show()
