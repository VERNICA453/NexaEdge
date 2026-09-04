import os
import numpy as np

# ==============================
# PATHS
# ==============================

FEATURES_DIR = "Features"
SPLIT_DIR = "Dataset_Split"
OUTPUT_DIR = "Combined_Features"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# Labels
LABELS = {
    "Noise": 0,
    "Positive": 1,
    "Unknown": 2
}

# ==============================
# FUNCTION TO LOAD FEATURES
# ==============================

def load_features(split_name):
    X = []
    y = []

    split_path = os.path.join(SPLIT_DIR, split_name)

    for category, label in LABELS.items():

        category_path = os.path.join(split_path, category)

        if not os.path.exists(category_path):
            print(f"Warning: {category_path} not found")
            continue

        for root, dirs, files in os.walk(category_path):

            for file in files:

                if not file.endswith(".npy"):
                    continue

                file_path = os.path.join(root, file)

                try:
                    feature = np.load(file_path)

                    # Make sure the feature has the expected shape
                    if feature.shape != (40, 251):
                        print(
                            f"Skipping {file_path} "
                            f"(shape {feature.shape})"
                        )
                        continue

                    X.append(feature)
                    y.append(label)

                except Exception as e:
                    print(f"Error reading {file_path}: {e}")

    if len(X) == 0:
        return np.empty((0, 40, 251), dtype=np.float32), np.empty((0,), dtype=np.int64)

    X = np.array(X, dtype=np.float32)
    y = np.array(y, dtype=np.int64)

    return X, y


# ==============================
# PROCESS TRAIN / VALIDATION / TEST
# ==============================

for split in ["Train", "Validation", "Test"]:

    print("\n==============================")
    print(f"Processing {split}")
    print("==============================")

    X, y = load_features(split)

    print("X shape:", X.shape)
    print("y shape:", y.shape)

    # Save
    np.save(
        os.path.join(OUTPUT_DIR, f"X_{split.lower()}.npy"),
        X
    )

    np.save(
        os.path.join(OUTPUT_DIR, f"y_{split.lower()}.npy"),
        y
    )

    print(f"{split} features saved.")


print("\n================================")
print("FEATURE COMBINATION COMPLETED!")
print("================================")