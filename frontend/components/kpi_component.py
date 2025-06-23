import streamlit as st
import requests

def kpi_forecast_ui():
    st.header("📈 KPI Forecasting (Water, Energy, etc.)")
    uploaded_file = st.file_uploader("Upload a CSV file with 'Year' and 'KPI Value'", type="csv")

    if uploaded_file:
        st.success("File uploaded successfully!")
        if st.button("Forecast Next Year"):
            files = {"file": uploaded_file.getvalue()}
            res = requests.post("http://localhost:8000/api/forecast", files=files)
            if res.status_code == 200:
                data = res.json()
                st.success(f"📊 Predicted {data['predicted_year']} KPI: {round(data['predicted_value'], 2)}")
            else:
                st.error("Prediction failed. Check CSV format.")
