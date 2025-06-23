import streamlit as st
import pandas as pd
import altair as alt

def kpi_dashboard_ui():
    st.title("📊 Smart City KPI Dashboard")

    file = st.file_uploader("Upload KPI Dashboard Data (CSV with KPI, Value)", type="csv")

    if file:
        df = pd.read_csv(file)

        st.subheader("📌 Key Performance Indicators")
        for index, row in df.iterrows():
            st.metric(label=row["KPI"], value=row["Value"])

        st.subheader("📈 Visual Overview")
        chart = alt.Chart(df).mark_bar().encode(
            x="KPI",
            y="Value",
            color="KPI"
        ).properties(width=600)
        st.altair_chart(chart)

    else:
        st.warning("Upload a KPI CSV file to see the dashboard.")
