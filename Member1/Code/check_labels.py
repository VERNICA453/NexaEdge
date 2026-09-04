import numpy as np

y = np.load("y.npy")

label_names = {
    0: "Noise",
    1: "Positive",
    2: "Unknown"
}

print("Checking label distribution...\n")

total = len(y)

for label, name in label_names.items():

    count = np.sum(y == label)
    percentage = (count / total) * 100

    print(f"{name}: {count} files ({percentage:.1f}%)")

print("\nTotal files:", total)