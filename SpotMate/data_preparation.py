import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# -----------------------------
# STEP 1: Load the dataset
# -----------------------------
print("Loading dataset...")
df = pd.read_csv("parking_dataset.csv")

# -----------------------------
# STEP 2: Sort the data
# -----------------------------
print("Sorting dataset by zone, day, and hour...")
df = df.sort_values(by=["zone_id", "day", "hour"])

# -----------------------------
# STEP 3: Extract occupancy
# -----------------------------
occupancy = df["occupancy"].values

# -----------------------------
# STEP 4: Normalize (0–100 → 0–1)
# -----------------------------
occupancy = occupancy / 100.0

# -----------------------------
# STEP 5: Create sequences
# -----------------------------
sequence_length = 3   # past 3 hours → next hour
X = []
y = []

for i in range(len(occupancy) - sequence_length):
    X.append(occupancy[i:i + sequence_length])
    y.append(occupancy[i + sequence_length])

X = np.array(X)
y = np.array(y)

# -----------------------------
# STEP 6: Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# STEP 7: Print results
# -----------------------------
print("\nDATA PREPARATION COMPLETE ✅")
print("--------------------------------")
print("Total samples       :", X.shape[0])
print("Input shape (X)     :", X.shape)
print("Output shape (y)    :", y.shape)
print("Training samples   :", X_train.shape[0])
print("Testing samples    :", X_test.shape[0])

print("\nSample input (X[0]):", X[0])
print("Sample output (y[0]):", y[0])
df.to_csv("parking_dataset_sorted.csv", index=False)
print("Sorted dataset saved as parking_dataset_sorted.csv")
