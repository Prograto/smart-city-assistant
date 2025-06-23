import streamlit as st
from components.chat_component import chat_ui
from components.summary_component import summary_ui
from components.kpi_component import kpi_forecast_ui
from components.feedback_component import feedback_form_ui
from components.eco_tips_component import eco_tips_ui
from components.anomaly_component import anomaly_detector_ui
from components.semantic_search_component import semantic_search_ui
from components.kpi_dashboard_component import kpi_dashboard_ui

st.set_page_config(page_title="Smart City Assistant", layout="wide")

st.sidebar.title("Assistant Modules")
selection = st.sidebar.radio("Go to", ["Chat Assistant", "Policy Summarizer", "KPI Forecasting", "Citizen Feedback", "Eco Tips Generator", "Anomaly Detection", "Policy Search", "KPI Dashboard"])

if selection == "Chat Assistant":
    chat_ui()
elif selection == "Policy Summarizer":
    summary_ui()
elif selection == "KPI Forecasting":
    kpi_forecast_ui()
elif selection == "Citizen Feedback":
    feedback_form_ui()
elif selection == "Eco Tips Generator":
    eco_tips_ui()
elif selection == "Anomaly Detection":
    anomaly_detector_ui()
elif selection == "Policy Search":
    semantic_search_ui()
elif selection == "KPI Dashboard":
    kpi_dashboard_ui()

