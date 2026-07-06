import streamlit as st
import joblib
import numpy as np

# Page Configuration
st.set_page_config(
    page_title="Advertising Sales Prediction",
    page_icon="📈",
    layout="centered"
)

# Load Model and Scaler
model = joblib.load("sales_prediction_model.pkl")
scaler = joblib.load("scaler.pkl")

# Title
st.title("📈 Advertising Sales Prediction")

st.write(
    "Predict product sales based on advertising budgets across "
    "**TV**, **Radio**, and **Newspaper**."
)

st.divider()

# Input Form
with st.form("prediction_form"):

    tv = st.text_input("TV Advertising Budget", placeholder="Enter TV budget")

    radio = st.text_input("Radio Advertising Budget", placeholder="Enter Radio budget")

    newspaper = st.text_input("Newspaper Advertising Budget", placeholder="Enter Newspaper budget")

    submit = st.form_submit_button("Predict Sales")

# Prediction
if submit:
    try:
        tv = float(tv)
        radio = float(radio)
        newspaper = float(newspaper)

        data = np.array([[tv, radio, newspaper]])
        data = scaler.transform(data)

        prediction = model.predict(data)

        st.success(f"📊 Predicted Sales: **{prediction[0]:.2f} units**")

    except ValueError:
        st.error("⚠️ Please enter valid numeric values.")

st.divider()

st.caption("Developed using Streamlit and Scikit-learn")