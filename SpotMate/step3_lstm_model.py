import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense

# -----------------------------
# 1. Load the sorted dataset
# -----------------------------
print("Loading dataset...")
df = pd.read_csv("parking_dataset_sorted.csv")

df = df.sort_values(by=["zone_id", "day", "hour"])

# -----------------------------
# 2. Extract and normalize occupancy
# -----------------------------
occupancy = df["occupancy"].values / 100.0

# -----------------------------
# 3. Create sequences
# -----------------------------
sequence_length = 3
X, y = [], []

for i in range(len(occupancy) - sequence_length):
    X.append(occupancy[i:i + sequence_length])
    y.append(occupancy[i + sequence_length])

X = np.array(X)
y = np.array(y)

# -----------------------------
# 4. Reshape for LSTM
# -----------------------------
# Shape: [samples, timesteps, features]
X = X.reshape((X.shape[0], X.shape[1], 1))

# -----------------------------
# 5. Train-test split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 6. Build LSTM model
# -----------------------------
model = Sequential()
model.add(LSTM(50, activation="relu", input_shape=(sequence_length, 1)))
model.add(Dense(1))

model.compile(optimizer="adam", loss="mse")

# -----------------------------
# 7. Train model
# -----------------------------
print("Training model...")
history = model.fit(
    X_train,
    y_train,
    epochs=20,
    batch_size=32,
    validation_split=0.1,
    verbose=1
)

# -----------------------------
# 8. Evaluate model
# -----------------------------
loss = model.evaluate(X_test, y_test, verbose=0)
print("\nTest Mean Squared Error:", loss)

# -----------------------------
# 9. Plot training history
# -----------------------------
plt.plot(history.history["loss"], label="Training Loss")
plt.plot(history.history["val_loss"], label="Validation Loss")
plt.xlabel("Epoch")
plt.ylabel("Loss")
plt.title("LSTM Training Loss")
plt.legend()
plt.show()

# -----------------------------
# 10. Sample predictions
# -----------------------------
predictions = model.predict(X_test[:5])

print("\nSample Predictions:")
for i in range(5):
    print(
        f"Predicted: {predictions[i][0]:.2f} | Actual: {y_test[i]:.2f}"
    )
