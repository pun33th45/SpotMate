# backend_predictor.py

import os
import numpy as np
import pandas as pd
import streamlit as st

# ---------------------------------------------------
# Resolve paths relative to this file (works on any OS / Streamlit Cloud)
# ---------------------------------------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, "data")

DATASET_PATH = os.path.join(DATA_DIR, "parking_dataset_sorted.csv")
MODEL_PATH = os.path.join(DATA_DIR, "cnn_lstm_parking_model.keras")


# ---------------------------------------------------
# Cached loaders — load once, reuse across reruns
# ---------------------------------------------------

@st.cache_data(show_spinner=False)
def load_dataset():
    """Load the parking dataset with a safe existence check."""
    if not os.path.isfile(DATASET_PATH):
        st.error(f"Dataset not found at: {DATASET_PATH}")
        return pd.DataFrame(columns=["zone_id", "day", "hour", "occupancy", "is_weekend"])
    return pd.read_csv(DATASET_PATH)


@st.cache_resource(show_spinner=False)
def load_keras_model():
    """Load the CNN-LSTM model with a safe existence check."""
    if not os.path.isfile(MODEL_PATH):
        st.error(f"Model file not found at: {MODEL_PATH}")
        return None
    from tensorflow.keras.models import load_model
    return load_model(MODEL_PATH)


# ---------------------------------------------------
# Helper: convert 12-hour time to 24-hour
# ---------------------------------------------------

def convert_to_24h(hour, am_pm):
    hour = int(hour)

    if am_pm == "PM" and hour != 12:
        return hour + 12
    if am_pm == "AM" and hour == 12:
        return 0
    return hour


# ---------------------------------------------------
# CORE FUNCTION (THIS IS THE HEART OF THE PROJECT)
# ---------------------------------------------------

def predict_parking_occupancy(zone_id, day, hour_24):
    """
    Uses historical data + CNN-LSTM to predict next-hour occupancy.
    Returns predicted occupancy (0-100) or None on failure.
    """

    df = load_dataset()
    model = load_keras_model()

    # If model or dataset failed to load, return None gracefully
    if model is None or df.empty:
        return None

    # We need last 3 hours
    past_hours = [hour_24 - 3, hour_24 - 2, hour_24 - 1]

    # Edge case (early hours)
    if min(past_hours) < 0:
        return None

    # Filter dataset
    history = df[
        (df["zone_id"] == zone_id) &
        (df["day"] == day) &
        (df["hour"].isin(past_hours))
    ].sort_values("hour")

    # If we don't have exactly 3 records -> can't predict
    if len(history) != 3:
        return None

    # Extract occupancies
    occupancies = history["occupancy"].values

    # Normalize
    X = occupancies / 100.0

    # Reshape for CNN + LSTM -> (1, 3, 1)
    X = X.reshape(1, 3, 1)

    # Predict
    prediction = model.predict(X, verbose=0)[0][0]

    # Denormalize
    predicted_occupancy = round(float(prediction) * 100, 2)

    return predicted_occupancy
