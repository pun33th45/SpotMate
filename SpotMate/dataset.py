import pandas as pd
import random

data = []

zones = {
    "Z1": "office",
    "Z2": "mall",
    "Z3": "residential",
    "Z4": "hospital",
    "Z5": "station"
}

for day in range(1, 31):
    is_weekend = 1 if day % 7 in [6, 0] else 0

    for hour in range(24):
        for zone, ztype in zones.items():

            if ztype == "office":
                base = random.randint(70, 90) if 9 <= hour <= 17 else random.randint(10, 30)

            elif ztype == "mall":
                base = random.randint(75, 95) if 17 <= hour <= 22 else random.randint(20, 40)
                if is_weekend:
                    base += 5

            elif ztype == "residential":
                base = random.randint(70, 90) if hour >= 20 or hour <= 6 else random.randint(30, 50)

            elif ztype == "hospital":
                base = random.randint(60, 80)

            elif ztype == "station":
                base = random.randint(70, 90) if hour in [7,8,9,17,18,19] else random.randint(30, 50)

            occupancy = min(base, 100)

            data.append([zone, day, hour, occupancy, is_weekend])

df = pd.DataFrame(
    data,
    columns=["zone_id", "day", "hour", "occupancy", "is_weekend"]
)

# 🔴 CHANGE THIS PATH if needed
df.to_csv("parking_dataset.csv", index=False)

print("CSV file created successfully!")
print("Total records:", df.shape[0])