import wave
from pathlib import Path

PROCESSED_FOLDER = Path("Processed")

wav_files = list(PROCESSED_FOLDER.rglob("*.wav"))

print("Checking processed audio...\n")
print("Total WAV files:", len(wav_files))

print("\nFirst 5 files:\n")

for file in wav_files[:5]:

    with wave.open(str(file), "rb") as audio:

        sample_rate = audio.getframerate()
        channels = audio.getnchannels()
        sample_width = audio.getsampwidth()
        frames = audio.getnframes()

        duration = frames / sample_rate

    print(f"File: {file.name}")
    print(f"Sample rate: {sample_rate} Hz")
    print(f"Channels: {channels}")
    print(f"Sample width: {sample_width * 8} bits")
    print(f"Duration: {duration:.2f} seconds")
    print("-------------------------")