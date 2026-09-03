import os
import librosa

# Dataset location
DATASET_PATH = "Dataset_Split"

audio_files = []

# Search all folders for WAV files
for root, folders, files in os.walk(DATASET_PATH):
    for file in files:
        if file.lower().endswith(".wav"):
            audio_files.append(os.path.join(root, file))

print("================================")
print("DAY 1 AUDIO PROCESSING")
print("================================")

print("Total WAV files found:", len(audio_files))

if len(audio_files) > 0:

    # Select the first audio file
    file_path = audio_files[0]

    print("\nTesting audio file:")
    print(file_path)

    # Load audio at 16 kHz
    audio, sr = librosa.load(file_path, sr=16000)

    print("\nSample Rate:", sr)
    print("Number of Samples:", len(audio))

    # Calculate duration
    duration = len(audio) / sr
    print("Duration:", duration, "seconds")

    # 30 ms window
    window_size = int(sr * 0.030)

    print("30 ms Window Size:", window_size, "samples")

    # Divide audio into 30 ms windows
    windows = []

    for start in range(0, len(audio), window_size):

        window = audio[start:start + window_size]

        if len(window) == window_size:
            windows.append(window)

    print("Number of Complete 30 ms Windows:", len(windows))

    print("\nDAY 1 COMPLETED SUCCESSFULLY!")

else:
    print("\nNo WAV files found!")