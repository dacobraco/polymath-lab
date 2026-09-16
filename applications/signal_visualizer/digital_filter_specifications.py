import numpy as np
import matplotlib.pyplot as plt

sample_rate = 200.0
passband_edge = 20.0
stopband_edge = 50.0
maximum_passband_loss_db = 1.0
minimum_stopband_attenuation_db = 40.0

nyquist_frequency = sample_rate / 2.0
transition_width = stopband_edge - passband_edge

normalized_passband_edge = passband_edge / nyquist_frequency
normalized_stopband_edge = stopband_edge / nyquist_frequency

minimum_passband_amplitude = 10 ** (-maximum_passband_loss_db / 20.0)
maximum_stopband_amplitude = 10 ** (-minimum_stopband_attenuation_db / 20.0)

print("Nyquist frequency:", nyquist_frequency, "Hz")
print("Transition width:", transition_width, "Hz")
print("Normalized passband edge:", normalized_passband_edge)
print("Normalized stopband edge:", normalized_stopband_edge)
print("Minimum passband amplitude:", minimum_passband_amplitude)
print("Maximum stopband amplitude:", maximum_stopband_amplitude)

figure, axis = plt.subplots(figsize=(10, 6))

axis.fill_between([0.0, passband_edge], -1.0, 0.0, color="green", alpha=0.3, label="Allowed passband")
axis.fill_between([0.0, passband_edge], -80.0, -1.0, color="red", alpha=0.15, label="Forbidden region")

axis.axvspan(passband_edge, stopband_edge, color="gray", alpha=0.2, label="Transition band")

axis.fill_between([stopband_edge, nyquist_frequency], -80.0, -40.0, color="green", alpha=0.3, label="Allowed stopband")
axis.fill_between([stopband_edge, nyquist_frequency], -40.0, 0.0, color="red", alpha=0.15)

axis.axvline(passband_edge, color="black", linestyle="--")
axis.axvline(stopband_edge, color="black", linestyle="--")
axis.axhline(-maximum_passband_loss_db, color="green", linestyle="--")
axis.axhline(-minimum_stopband_attenuation_db, color="green", linestyle="--")

axis.set_xlim(0.0, nyquist_frequency)
axis.set_ylim(-80.0, 2.0)
axis.set_xlabel("Frequency [Hz]")
axis.set_ylabel("Magnitude [dB]")
axis.set_title("Low-pass Filter Specification Mask")
axis.grid(True, alpha=0.3)
axis.legend()

figure.tight_layout()
figure.savefig("filter_specification_mask.png", dpi=150)
plt.show()

print("Specification mask saved: filter_specification_mask.png")
test_frequencies = np.array([10.0, 20.0, 35.0, 50.0, 80.0])
test_magnitudes_db = np.array([-0.3, -0.8, -18.0, -42.0, -55.0])

passband_mask = test_frequencies <= passband_edge
stopband_mask = test_frequencies >= stopband_edge

passband_values_db = test_magnitudes_db[passband_mask]
stopband_values_db = test_magnitudes_db[stopband_mask]

passband_passed = np.all(passband_values_db >= -maximum_passband_loss_db)
stopband_passed = np.all(stopband_values_db <= -minimum_stopband_attenuation_db)
complete_specification_passed = passband_passed and stopband_passed

print("Passband passed:", passband_passed)
print("Stopband passed:", stopband_passed)
print("Complete specification passed:", complete_specification_passed)

assert np.isclose(nyquist_frequency, 100.0)
assert np.isclose(transition_width, 30.0)
assert np.isclose(normalized_passband_edge, 0.2)
assert np.isclose(normalized_stopband_edge, 0.5)
assert np.isclose(minimum_passband_amplitude, 10 ** (-1.0 / 20.0))
assert np.isclose(maximum_stopband_amplitude, 0.01)

assert passband_passed
assert stopband_passed
assert complete_specification_passed

print("Filter specification checks: PASSED")
