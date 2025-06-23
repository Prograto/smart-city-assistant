import streamlit as st
import requests
import pandas as pd

def anomaly_detector_ui():
    st.header("⚠️ KPI Anomaly Detector")

    file = st.file_uploader("Upload KPI CSV (e.g., energy, water data)", type="csv")

    if file and st.button("Detect Anomalies"):
        res = requests.post("http://localhost:8000/api/anomaly", files={"file": file.getvalue()})
        if res.status_code == 200:
            data = res.json()
            if data["count"] > 0:
                st.error(f"⚠️ {data['count']} anomalies found!")
                st.dataframe(pd.DataFrame(data["anomalies"]))
            else:
                st.success("✅ No anomalies found. All values look normal!")
        else:
            st.error("Error detecting anomalies.")
