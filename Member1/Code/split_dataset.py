import os
import random
import shutil

SOURCE_DIR = "Augmented"
OUTPUT_DIR = "Dataset_Split"

CATEGORIES = ["Positive", "Unknown", "Noise"]

random.seed(42)


# ------------------------------------------------------------
# Find original files
# ------------------------------------------------------------

def is_original(filename):
    name = os.path.splitext(filename)[0].lower()

    return not (
        name.endswith("_noise")
        or name.endswith("_shift")
        or name.endswith("_volume")
    )


# ------------------------------------------------------------
# Create output folders
# ------------------------------------------------------------

for split in ["Train", "Validation", "Test"]:
    for category in CATEGORIES:
        os.makedirs(
            os.path.join(OUTPUT_DIR, split, category),
            exist_ok=True
        )


# ------------------------------------------------------------
# Process each category
# ------------------------------------------------------------

for category in CATEGORIES:

    category_path = os.path.join(SOURCE_DIR, category)

    # Each immediate parent folder is treated as a recording group.
    # We then identify the original files inside those folders.

    groups = []

    for root, dirs, files in os.walk(category_path):

        wav_files = [
            f for f in files
            if f.lower().endswith(".wav")
        ]

        original_files = [
            f for f in wav_files
            if is_original(f)
        ]

        for original in original_files:

            base = os.path.splitext(original)[0]

            related = []

            for f in wav_files:

                fbase = os.path.splitext(f)[0]

                if (
                    fbase == base
                    or fbase == base + "_noise"
                    or fbase == base + "_shift"
                    or fbase == base + "_volume"
                ):
                    related.append(
                        os.path.join(root, f)
                    )

            if related:
                groups.append(related)


    # --------------------------------------------------------
    # Shuffle groups
    # --------------------------------------------------------

    random.shuffle(groups)

    total = len(groups)

    train_count = int(total * 0.70)
    validation_count = int(total * 0.15)

    train_groups = groups[:train_count]

    validation_groups = groups[
        train_count:
        train_count + validation_count
    ]

    test_groups = groups[
        train_count + validation_count:
    ]


    splits = {
        "Train": train_groups,
        "Validation": validation_groups,
        "Test": test_groups
    }


    # --------------------------------------------------------
    # Copy files
    # --------------------------------------------------------

    for split_name, split_groups in splits.items():

        destination = os.path.join(
            OUTPUT_DIR,
            split_name,
            category
        )

        for group in split_groups:

            for source_file in group:

                filename = os.path.basename(source_file)

                destination_file = os.path.join(
                    destination,
                    filename
                )

                shutil.copy2(
                    source_file,
                    destination_file
                )


    # --------------------------------------------------------
    # Display results
    # --------------------------------------------------------

    print()
    print(category)
    print("-------------------------")
    print("Original groups:", total)
    print("Train:", len(train_groups))
    print("Validation:", len(validation_groups))
    print("Test:", len(test_groups))


print()
print("====================================")
print("DATASET SPLIT COMPLETED!")
print("====================================")
print()
print("Augmented folder was NOT modified.")
print("Dataset_Split has been created.")