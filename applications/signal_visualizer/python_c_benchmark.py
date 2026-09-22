import numpy as np
import time

number_of_samples = 1_000_000
signal = np.linspace(0.0, 1.0, number_of_samples, dtype=np.float64)
energy = 0

start_time = time.perf_counter()
for sample in signal:
    energy += sample * sample
end_time = time.perf_counter()

print("Energy:", energy)
print(f"Loop took {end_time - start_time} seconds.")
print("Number of bytes:", signal.nbytes)
