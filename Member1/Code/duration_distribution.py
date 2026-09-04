import wave
from pathlib import Path

PROCESSED_FOLDER = Path("Processed")

ranges = {
    "< 2 sec": 0,
    "2–3 sec": 0,
    "3–4 sec": 0,
    "4–5 sec": 0,
    "5–6 sec": 0,
    "6–8 sec": 0,
    "> 8 sec": 0
}

for file in PROCESSED_FOLDER.rglob("*.wav"):

    with wave.open(str(file), "rb") as audio:

        sample_rate = audio.getframerate()
        frames = audio.getnframes()
        duration = frames / sample_rate

    if duration < 2:
        ranges["< 2 sec"] += 1

    elif duration < 3:
        ranges["2–3 sec"] += 1

    elif duration < 4:
        ranges["3–4 sec"] += 1

    elif duration < 5:
        ranges["4–5 sec"] += 1

    elif duration < 6:
        ranges["5–6 sec"] += 1

    elif duration < 8:
        ranges["6–8 sec"] += 1

    else:
        ranges["> 8 sec"] += 1


print("Audio duration distribution:\n")

for duration_range, count in ranges.items():
    print(f"{duration_range}: {count} files")