import os
import librosa
import soundfile as sf
import numpy as np

# --------------------------------------------------
# 1. FOLDER SETTINGS
# --------------------------------------------------

INPUT_DIR = "Augmented"

CATEGORIES = ["Positive", "Unknown", "Noise"]


# --------------------------------------------------
# 2. AUDIO AUGMENTATION FUNCTIONS
# --------------------------------------------------

def change_volume(audio, factor):
    """Change the volume of an audio signal."""
    return audio * factor


def time_shift(audio, shift):
    """Shift the audio left or right."""
    return np.roll(audio, shift)


def add_noise(audio, noise_level=0.005):
    """Add a small amount of random noise."""
    noise = np.random.randn(len(audio))
    return audio + noise_level * noise


# --------------------------------------------------
# 3. PROCESS ALL AUDIO FILES
# --------------------------------------------------

for category in CATEGORIES:

    category_path = os.path.join(INPUT_DIR, category)

    if not os.path.exists(category_path):
        print(f"Folder not found: {category_path}")
        continue

    # Walk through all member/speaker folders
    for root, dirs, files in os.walk(category_path):

        for file in files:

            if not file.lower().endswith(".wav"):
                continue

            file_path = os.path.join(root, file)

            # Load audio
            audio, sample_rate = librosa.load(
                file_path,
                sr=None,
                mono=True
            )

            base_name = os.path.splitext(file)[0]

            # --------------------------------------------------
            # AUGMENTATION 1: VOLUME CHANGE
            # --------------------------------------------------

            volume_audio = change_volume(audio, 0.8)

            volume_path = os.path.join(
                root,
                base_name + "_volume.wav"
            )

            sf.write(
                volume_path,
                volume_audio,
                sample_rate
            )


            # --------------------------------------------------
            # AUGMENTATION 2: TIME SHIFT
            # --------------------------------------------------

            shift_amount = int(0.1 * sample_rate)

            shifted_audio = time_shift(
                audio,
                shift_amount
            )

            shift_path = os.path.join(
                root,
                base_name + "_shift.wav"
            )

            sf.write(
                shift_path,
                shifted_audio,
                sample_rate
            )


            # --------------------------------------------------
            # AUGMENTATION 3: ADD BACKGROUND-LIKE NOISE
            # --------------------------------------------------

            noisy_audio = add_noise(
                audio,
                noise_level=0.005
            )

            noise_path = os.path.join(
                root,
                base_name + "_noise.wav"
            )

            sf.write(
                noise_path,
                noisy_audio,
                sample_rate
            )

            print(f"Augmented: {file_path}")


print("\nData augmentation completed!")