import sounddevice as sd

def audio_callback(indata, frames, time, status):
    stats["blocks"] += 1
    stats["frames"] += frames
    if status.input_overflow:
        stats["overflows"] += 1

input_device = 3
sampling_frequency = 44100
channels = 1
block_size = 1024

stats = {"blocks": 0, "frames": 0, "overflows": 0}

with sd.InputStream(sampling_frequency, block_size, input_device, channels, dtype="float32", callback=audio_callback) as stream:
    input("Speak into the microphone. Press Enter to stop.\n")

print(stats)
