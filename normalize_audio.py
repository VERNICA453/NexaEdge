import wave
from pathlib import Path

PROCESSED_FOLDER = Path("Processed")
NORMALIZED_FOLDER = Path("Normalized")

TARGET_SAMPLE_RATE = 16000
TARGET_DURATION = 4
TARGET_FRAMES = TARGET_SAMPLE_RATE * TARGET_DURATION

wav_files = list(PROCESSED_FOLDER.rglob("*.wav"))

print("Starting duration normalization...")
print(f"Target duration: {TARGET_DURATION} seconds")
print(f"Files to process: {len(wav_files)}\n")

for file in wav_files:

    relative_path = file.relative_to(PROCESSED_FOLDER)
    output_file = NORMALIZED_FOLDER / relative_path

    output_file.parent.mkdir(parents=True, exist_ok=True)

    with wave.open(str(file), "rb") as audio:

        sample_rate = audio.getframerate()
        channels = audio.getnchannels()
        sample_width = audio.getsampwidth()

        frames = audio.readframes(TARGET_FRAMES)

    current_frames = len(frames) // (channels * sample_width)

    if current_frames < TARGET_FRAMES:

        silence_frames = TARGET_FRAMES - current_frames

        silence = b"\x00" * (
            silence_frames * channels * sample_width
        )

        frames += silence

    with wave.open(str(output_file), "wb") as output:

        output.setnchannels(channels)
        output.setsampwidth(sample_width)
        output.setframerate(sample_rate)
        output.writeframes(frames)

    print(f"Processed: {file.name}")

print("\nDuration normalization completed!")