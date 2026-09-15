import numpy as np
import sounddevice as sd
import soundfile as sf

sample_rate = 44100
recording_duration = 4.0
channel_count = 1
print("Available audio devices:")
print(sd.query_devices())
input_device_index = int(input("Enter microphone device index: "))

frame_count = int(sample_rate * recording_duration)

input("Press Enter when ready...")

print("Recording...")

recording = sd.rec(frame_count, samplerate=sample_rate, channels=channel_count, dtype="float64", device=input_device_index)
sd.wait()

print("Recording finished.")

largest_amplitude = np.max(np.abs(recording))
output_path = "recorded_voice.wav"

sf.write(output_path, recording, sample_rate, subtype="PCM_16")

print("WAV written:", output_path)
print("Sample rate:", sample_rate)
print("Duration:", recording_duration)
print("Sample frames:", frame_count)
print("Channels:", channel_count)
print("Recording array shape:", recording.shape)
print("Largest absolute amplitude:", largest_amplitude)
