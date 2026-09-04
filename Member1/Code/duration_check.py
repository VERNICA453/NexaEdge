import wave
from pathlib import Path

PROCESSED_FOLDER = Path("Processed")

durations = []

for file in PROCESSED_FOLDER.rglob("*.wav"):

    with wave.open(str(file), "rb") as audio:

        sample_rate = audio.getframerate()
        frames = audio.getnframes()

        duration = frames / sample_rate
        durations.append(duration)

print("Total files:", len(durations))

print(f"Shortest audio: {min(durations):.2f} seconds")
print(f"Longest audio: {max(durations):.2f} seconds")
print(f"Average duration: {sum(durations) / len(durations):.2f} seconds")