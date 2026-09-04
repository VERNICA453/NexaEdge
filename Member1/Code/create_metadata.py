import csv
from pathlib import Path

FEATURE_FOLDER = Path("Features")
OUTPUT_FILE = Path("metadata.csv")

LABELS = {
    "Noise": 0,
    "Positive": 1,
    "Unknown": 2
}

rows = []

for feature_file in FEATURE_FOLDER.rglob("*.npy"):

    relative = feature_file.relative_to(FEATURE_FOLDER)
    parts = relative.parts

    # Expected structure:
    # Class / Member / optional subfolders / file.npy

    if len(parts) < 3:
        print(f"Skipping: {feature_file}")
        continue

    class_name = parts[0]
    member_name = parts[1]

    if class_name not in LABELS:
        print(f"Unknown class: {feature_file}")
        continue

    rows.append({
        "feature_path": str(relative),
        "label": class_name,
        "label_id": LABELS[class_name],
        "member": member_name
    })

with open(
    OUTPUT_FILE,
    "w",
    newline="",
    encoding="utf-8"
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "feature_path",
            "label",
            "label_id",
            "member"
        ]
    )

    writer.writeheader()
    writer.writerows(rows)

print("Metadata created!")
print("Total records:", len(rows))
print("Saved as:", OUTPUT_FILE)