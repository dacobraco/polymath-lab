import numpy as np

experiments_number = 100_000
amplitude = 1.0
std = 0.4
threshold = 0.5

rng = np.random.default_rng(42)
H0 = rng.normal(0, std, experiments_number)
H1 = amplitude + rng.normal(0, std, experiments_number)

false_alarms = np.sum(H0 > threshold)
detections = np.sum(H1 > threshold)

false_alarm_probability = false_alarms / experiments_number
detection_probability = detections / experiments_number
print("False alarm probability:", false_alarm_probability)
print("Detection probability:", detection_probability)

estimated_amplitude = np.mean(H1)
print(f"Estiamted amplitude: {estimated_amplitude}\tExact amplitude: {amplitude}")
estimation_error = np.abs(amplitude - estimated_amplitude)
print("Estimation error:", estimation_error)
