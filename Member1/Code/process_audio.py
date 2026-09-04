import os
from pathlib import Path
import imageio_ffmpeg

RAW_FOLDER = Path("raw")
PROCESSED_FOLDER = Path("Processed")

FFMPEG = imageio_ffmpeg.get_ffmpeg_exe()

print("Raw folder:", RAW_FOLDER)
print("Processed folder:", PROCESSED_FOLDER)
print("FFmpeg:", FFMPEG)


AUDIO_EXTENSIONS = {".mp3", ".m4a", ".wav"}

audio_files = []

for file in RAW_FOLDER.rglob("*"):
    if file.is_file() and file.suffix.lower() in AUDIO_EXTENSIONS:
        audio_files.append(file)

print("Audio files found:", len(audio_files))

import subprocess

print("\nStarting audio conversion...\n")

for file in audio_files:

    # Find the category and member folder
    relative_path = file.relative_to(RAW_FOLDER)

    # Create the same folder structure inside Processed
    output_file = PROCESSED_FOLDER / relative_path.with_suffix(".wav")

    output_file.parent.mkdir(parents=True, exist_ok=True)

    # Convert to WAV, 16 kHz, mono
    command = [
        FFMPEG,
        "-y",
        "-i", str(file),
        "-ar", "16000",
        "-ac", "1",
        "-c:a", "pcm_s16le",
        str(output_file)
    ]

    subprocess.run(
        command,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    print(f"Converted: {file.name}")

print("\nAudio conversion completed!")