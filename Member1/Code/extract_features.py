import numpy as np
import librosa
from pathlib import Path

NORMALIZED_FOLDER = Path("Normalized")
FEATURE_FOLDER = Path("Features")

SAMPLE_RATE = 16000
N_MELS = 40
N_FFT = 512
HOP_LENGTH = 256

audio_files = list(NORMALIZED_FOLDER.rglob("*.wav"))

print("Starting feature extraction...")
print("Audio files found:", len(audio_files))

for file in audio_files:

    # Load audio
    audio, sr = librosa.load(
        file,
        sr=SAMPLE_RATE,
        mono=True
    )

    # Create Mel spectrogram
    mel = librosa.feature.melspectrogram(
        y=audio,
        sr=sr,
        n_fft=N_FFT,
        hop_length=HOP_LENGTH,
        n_mels=N_MELS
    )

    # Convert to decibels
    mel_db = librosa.power_to_db(
        mel,
        ref=np.max
    )

    # Preserve folder structure
    relative_path = file.relative_to(NORMALIZED_FOLDER)

    output_file = (
        FEATURE_FOLDER /
        relative_path.with_suffix(".npy")
    )

    output_file.parent.mkdir(
        parents=True,
        exist_ok=True
    )

    # Save feature
    np.save(output_file, mel_db)

    print(f"Extracted: {file.name}")

print("\nFeature extraction completed!")