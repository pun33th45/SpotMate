import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model

# -----------------------------
# Page configuration
# -----------------------------
st.set_page_config(
    page_title="ParkMatrix AI",
    page_icon="🚗",
    layout="centered"
)

# -----------------------------
# Load trained model (KERAS ONLY)
# -----------------------------
@st.cache_resource
def load_trained_model():
    return load_model("cnn_lstm_parking_model.keras")

model = load_trained_model()

# -----------------------------
# Header
# -----------------------------
st.markdown(
    """
    <h1 style="text-align:center;">🚗 ParkMatrix AI</h1>
    <h4 style="text-align:center; color:gray;">
    Intelligent Urban Parking Demand Prediction
    </h4>
    <hr>
    """,
    unsafe_allow_html=True
)

# -----------------------------
# Input section
# -----------------------------
st.subheader("📥 Enter Recent Parking Data")

zone = st.selectbox(
    "Select Parking Zone",
    [
        "Z1 – Office Area",
        "Z2 – Shopping Mall",
        "Z3 – Residential Area",
        "Z4 – Hospital",
        "Z5 – Railway Station"
    ]
)

col1, col2, col3 = st.columns(3)

with col1:
    h1 = st.slider("Occupancy 3 Hours Ago (%)", 0, 100, 30)

with col2:
    h2 = st.slider("Occupancy 2 Hours Ago (%)", 0, 100, 40)

with col3:
    h3 = st.slider("Occupancy 1 Hour Ago (%)", 0, 100, 50)

# -----------------------------
# Prediction
# -----------------------------
st.markdown("---")

if st.button("🔮 Predict Parking Demand", use_container_width=True):

    input_data = np.array([[h1 / 100, h2 / 100, h3 / 100]])
    input_data = input_data.reshape((1, 3, 1))

    prediction = model.predict(input_data)
    predicted_value = prediction[0][0] * 100

    st.subheader("📊 Prediction Result")

    st.metric(
        label="Predicted Parking Occupancy",
        value=f"{predicted_value:.2f} %"
    )

    if predicted_value >= 80:
        st.error("🚨 Very High Demand — Parking likely FULL")
    elif predicted_value >= 50:
        st.warning("⚠️ Moderate Demand — Limited availability")
    else:
        st.success("✅ Low Demand — Parking spaces AVAILABLE")

# -----------------------------
# Footer
# -----------------------------
st.markdown(
    """
    <hr>
    <p style="text-align:center; color:gray; font-size:14px;">
    ParkMatrix AI • CNN–LSTM Spatio-Temporal Model • Mini Project
    </p>
    """,
    unsafe_allow_html=True
)
