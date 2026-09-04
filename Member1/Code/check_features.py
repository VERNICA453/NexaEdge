import numpy as np
from pathlib import Path

FEATURE_FOLDER = Path("Features")

feature_files = list(FEATURE_FOLDER.rglob("*.npy"))

print("Checking feature files...\n")
print("Total feature files:", len(feature_files))

shapes = {}

for file in feature_files:

    feature = np.load(file)

    shape = feature.shape

    if shape not in shapes:
        shapes[shape] = 0

    shapes[shape] += 1


print("\nFeature shapes found:")

for shape, count in shapes.items():
    print(f"{shape} → {count} files")