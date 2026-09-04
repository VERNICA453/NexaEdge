import wave
from pathlib import Path

NORMALIZED_FOLDER = Path("Normalized")

durations = []

for file in NORMALIZED_FOLDER.rglob("*.wav"):

    with wave.open(str(file), "rb") as audio:

        sample_rate = audio.getframerate()
        frames = audio.getnframes()

        duration = frames / sample_rate
        durations.append(duration)

print("Checking normalized audio...\n")

print("Total files:", len(durations))

print(f"Shortest audio: {min(durations):.2f} seconds")
print(f"Longest audio: {max(durations):.2f} seconds")
print(f"Average duration: {sum(durations) / len(durations):.2f} seconds")