import numpy as np
import matplotlib.pyplot as plt
import bz2
from pathlib import Path

folder = Path(__file__).resolve().parent
file_path = next(folder.rglob("signal.bin.bz2"))

with bz2.open(file_path, "rb") as f:
    raw = np.frombuffer(f.read(), dtype=np.uint8)

print("Number of bytes:", len(raw))
print("First 10 values:", raw[:10])

i = (raw[0::2].astype(float) - 127.5) / 127.5
q = (raw[1::2].astype(float) - 127.5) / 127.5

iq = i + 1j * q

fs = 1_000_000
center_frequency = 433_800_000

print("IQ samples:", len(iq))
print("Duration:", len(iq) / fs, "seconds")

block_size = 1000

amplitude = np.abs(iq)
amplitude_blocks = amplitude.reshape(-1, block_size)

average_amplitude = np.mean(amplitude_blocks, axis=1)
time = (np.arange(len(average_amplitude)) + 0.5) * block_size / fs

start = int(0.275 * fs)
end = int(0.325 * fs)

iq_burst = iq[start:end]

print("Selected samples:", len(iq_burst))

spectrum = np.fft.fftshift(np.fft.fft(iq_burst))
frequencies = np.fft.fftshift(np.fft.fftfreq(len(iq_burst), d=1/fs))

rf_frequencies = center_frequency + frequencies
magnitude_db = 20 * np.log10(np.abs(spectrum) / len(iq_burst) + 1e-12)

peak_index = np.argmax(magnitude_db)
peak_frequency = rf_frequencies[peak_index]

print("Peak frequency:", peak_frequency / 1e6, "MHz")
print("Offset:", (peak_frequency - center_frequency) / 1000, "kHz")

plt.figure(figsize=(11, 5))
plt.plot(rf_frequencies / 1e6, magnitude_db)
plt.xlabel("Frequency (MHz)")
plt.ylabel("Magnitude (dB)")
plt.title("Real RF Signal - Frequency Spectrum")
plt.grid(True)
plt.tight_layout()

plt.figure(figsize=(11, 5))
plt.plot(time, average_amplitude)
plt.xlabel("Time (s)")
plt.ylabel("Average magnitude")
plt.title("Real RF Signal - Amplitude vs Time")
plt.grid(True)
plt.tight_layout()

burst_time = np.arange(len(iq_burst)) / fs * 1000
burst_amplitude = np.abs(iq_burst)

threshold = 0.35
detected_signal = (burst_amplitude > threshold).astype(int)

changes = np.diff(detected_signal)

starts = np.where(changes == 1)[0] + 1
ends = np.where(changes == -1)[0] + 1

print("Starts:", starts[:10])
print("Ends:", ends[:10])

pulse_durations = (ends - starts) / fs * 1000

print("Pulse durations (ms):")
print(np.round(pulse_durations[:20], 3))

pause_durations = (starts[1:] - ends[:-1]) / fs * 1000

print("Pause durations (ms):")
print(np.round(pause_durations[:20], 3))

pulse_types = np.where(pulse_durations < 1.0, "S", "L")
pause_types = np.where(pause_durations < 1.0, "S", "L")

for k in range(min(20, len(pause_types))):
    print(f"{k+1}: ON={pulse_types[k]}, OFF={pause_types[k]}")

full_detected = (np.abs(iq) > 0.35).astype(int)

transitions = np.diff(full_detected)

all_starts = np.where(transitions == 1)[0] + 1
all_ends = np.where(transitions == -1)[0] + 1

gaps_ms = (all_starts[1:] - all_ends[:-1]) / fs * 1000

large_gaps = np.where(gaps_ms > 10)[0]

print("Large gap indices:", large_gaps)
print("Large gap durations (ms):", np.round(gaps_ms[large_gaps], 2))
print("Number of bursts:", len(large_gaps) + 1)

burst_starts = np.split(all_starts, large_gaps + 1)
burst_ends = np.split(all_ends, large_gaps + 1)

for k, (s, e) in enumerate(zip(burst_starts, burst_ends), 1):
    durations = (e - s) / fs * 1000
    pattern = "".join(np.where(durations < 1, "S", "L"))
    print(f"Burst {k}: {len(durations)} pulses | {pattern}")

plt.figure(figsize=(11, 5))
plt.plot(burst_time, burst_amplitude)
plt.xlim(5, 15)
plt.xlabel("Time (ms)")
plt.ylabel("Magnitude")
plt.title("Real RF Signal - Digital Pulses")
plt.grid(True)
plt.tight_layout()

plt.figure(figsize=(11, 4))
plt.step(burst_time, detected_signal, where="post")
plt.xlim(5, 15)
plt.ylim(-0.1, 1.1)
plt.xlabel("Time (ms)")
plt.ylabel("Detected state")
plt.title("OOK Signal Detection")
plt.grid(True)
plt.show()
