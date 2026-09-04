import os

RAW_FOLDER = "raw"

audio_extensions = (".wav", ".mp3", ".flac", ".m4a", ".ogg")

total_files = 0

print("Scanning audio dataset...\n")

for category in os.listdir(RAW_FOLDER):

    category_path = os.path.join(RAW_FOLDER, category)

    if not os.path.isdir(category_path):
        continue

    category_count = 0

    for root, folders, files in os.walk(category_path):

        for file in files:

            if file.lower().endswith(audio_extensions):

                category_count += 1
                total_files += 1

    print(f"{category}: {category_count} audio files")

print("\n-------------------------")
print(f"Total audio files: {total_files}")
print("-------------------------")