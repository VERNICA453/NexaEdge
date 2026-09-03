import os
from pathlib import Path
import numpy as np
import librosa

INPUT_DIR = Path("Dataset_Split")
OUTPUT_DIR = Path("Split_Features")

SAMPLE_RATE = 16000
N_MFCC = 40
N_FFT = 512
HOP_LENGTH = 160

LABELS = {
    "Noise": 0,
    "Positive": 1,
    "Unknown": 2
}

for split in ["Train", "Validation", "Test"]:
    print("=" * 30)
    print("Processing", split)
    print("=" * 30)

    X = []
    y = []

    for label_name, label_value in LABELS.items():

        folder = INPUT_DIR / split / label_name

        if not folder.exists():
            print("Missing folder:", folder)
            continue

        wav_files = list(folder.rglob("*.wav"))

        print(label_name, "files:", len(wav_files))

        for wav_file in wav_files:
            try:
                audio, sr = librosa.load(
                    wav_file,
                    sr=SAMPLE_RATE,
                    mono=True
                )

                mfcc = librosa.feature.mfcc(
                    y=audio,
                    sr=sr,
                    n_mfcc=N_MFCC,
                    n_fft=N_FFT,
                    hop_length=HOP_LENGTH
                )

                # Make every feature exactly 251 frames
                if mfcc.shape[1] < 251:
                    mfcc = np.pad(
                        mfcc,
                        ((0, 0), (0, 251 - mfcc.shape[1])),
                        mode="constant"
                    )
                else:
                    mfcc = mfcc[:, :251]

                X.append(mfcc.astype(np.float32))
                y.append(label_value)

            except Exception as e:
                print("ERROR:", wav_file)
                print(e)

    if X:
        X = np.array(X, dtype=np.float32)
        y = np.array(y, dtype=np.int64)
    else:
        X = np.empty((0, 40, 251), dtype=np.float32)
        y = np.empty((0,), dtype=np.int64)

    output_folder = OUTPUT_DIR / split
    output_folder.mkdir(parents=True, exist_ok=True)

    np.save(output_folder / "X.npy", X)
    np.save(output_folder / "y.npy", y)

    print()
    print("X shape:", X.shape)
    print("y shape:", y.shape)
    print("Saved:", output_folder)
    print()

print("=" * 30)
print("FEATURE EXTRACTION COMPLETED!")
print("=" * 30)
