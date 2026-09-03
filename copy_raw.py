import os
import shutil

categories = ["Positive", "Unknown", "Noise"]

for category in categories:
    source = category
    destination = os.path.join("raw", category)

    os.makedirs(destination, exist_ok=True)

    for member in os.listdir(source):
        source_member = os.path.join(source, member)
        destination_member = os.path.join(destination, member)

        if os.path.isdir(source_member):
            shutil.copytree(
                source_member,
                destination_member,
                dirs_exist_ok=True
            )

    print(f"{category} copied successfully!")

print("\nDone! All recordings are now inside raw.")