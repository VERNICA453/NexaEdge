import numpy as np
from pathlib import Path

FEATURE_FOLDER = Path("Features")

X = []
y = []

label_map = {
    "Noise": 0,
    "Positive": 1,
    "Unknown": 2
}

feature_files = list(FEATURE_FOLDER.rglob("*.npy"))

print("Creating ML dataset...")
print("Feature files found:", len(feature_files))

for file in feature_files:

    # Find the class folder anywhere above the file
    class_name = None

    for parent in file.parents:

        if parent.name in label_map:
            class_name = parent.name
            break

    if class_name is None:
        print(f"Skipping file: {file}")
        continue

    feature = np.load(file)

    label = label_map[class_name]

    X.append(feature)
    y.append(label)

X = np.array(X)
y = np.array(y)

print("\nDataset created!")

print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nLabels:")
print("0 = Noise")
print("1 = Positive")
print("2 = Unknown")

np.save("X.npy", X)
np.save("y.npy", y)

print("\nSaved:")
print("X.npy")
print("y.npy")