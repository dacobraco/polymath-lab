import numpy as np
import matplotlib.pyplot as plt

f = 100.0
noise_f = 900.0
amplitude = 0.5
noise_amplitude = 0.3
dc_offset = 1.65
adc_frequency = 500.0
adc_resolution = 12
v_ref = 3.3
duration = 0.05
fc = 150.0

t = np.linspace(0, duration, 5000)
adc_t = np.arange(0, duration, 1/adc_frequency)

H_f = 1 / (1 + 1j*(f / fc))
H_f_magnitude = np.abs(H_f)
H_f_phase = np.angle(H_f)

H_noise_f = 1 / (1 + 1j*(noise_f / fc))
H_noise_f_magnitude = np.abs(H_noise_f)
H_noise_f_phase = np.angle(H_noise_f)

signal = dc_offset + amplitude*np.sin(2*np.pi*f*t) + noise_amplitude*np.sin(2*np.pi*noise_f*t)
adc_signal = dc_offset + amplitude*np.sin(2*np.pi*f*adc_t) + noise_amplitude*np.sin(2*np.pi*noise_f*adc_t)

filtered_signal = dc_offset + amplitude*H_f_magnitude*np.sin(2*np.pi*f*t + H_f_phase) + noise_amplitude*H_noise_f_magnitude*np.sin(2*np.pi*noise_f*t + H_noise_f_phase)
filtered_adc_signal = dc_offset + amplitude*H_f_magnitude*np.sin(2*np.pi*f*adc_t + H_f_phase) + noise_amplitude*H_noise_f_magnitude*np.sin(2*np.pi*noise_f*adc_t + H_noise_f_phase)

step = v_ref / (2**adc_resolution)

adc_codes = np.round(filtered_adc_signal / step)
adc_codes = np.clip(adc_codes, 0, 2**adc_resolution - 1).astype(int)

reconstructed_voltage = adc_codes * step
quantization_error = filtered_adc_signal - reconstructed_voltage
max_error = np.max(np.abs(quantization_error))

print("ADC resolution:", adc_resolution, "bits")
print("ADC levels:", 2**adc_resolution)
print("Voltage step:", step, "V")
print("Maximum quantization error:", max_error * 1000, "mV")
print("ADC codes:", adc_codes)

plt.figure(figsize=(10, 7))

plt.subplot(2, 1, 1)
plt.plot(t, signal, label="Original analog signal")
plt.scatter(adc_t, adc_signal, color="red", label="ADC samples")
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("Before Anti-Aliasing Filter")
plt.ylim(0.7, 2.6)
plt.grid(True)
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, filtered_signal, label="Filtered analog signal")
plt.scatter(adc_t, filtered_adc_signal, color="red", label="ADC samples")
plt.xlabel("Time [s]")
plt.ylabel("Voltage [V]")
plt.title("After Anti-Aliasing Filter")
plt.ylim(0.7, 2.6)
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
