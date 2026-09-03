import os
from pathlib import Path

RAW_FOLDER = Path("raw")

audio_extensions = {".mp3", ".m4a", ".wav", ".flac", ".ogg"}

print("Inspecting audio files...\n")

total = 0

for category in RAW_FOLDER.iterdir():

    if not category.is_dir():
        continue

    print(f"\n===== {category.name} =====")

    for file in category.rglob("*"):

        if file.is_file() and file.suffix.lower() in audio_extensions:

            print(f"{file.name}  -->  {file.suffix.lower()}")
            total += 1

print("\n-------------------------")
print(f"Total audio files found: {total}")
print("-------------------------")