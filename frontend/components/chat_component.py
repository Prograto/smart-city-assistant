import streamlit as st
import requests

def chat_ui():
    st.header("💬 Smart City Chat Assistant")
    prompt = st.text_area("Ask something about sustainability or your city...")

    if st.button("Ask"):
        res = requests.post("http://localhost:8000/api/chat", json={"prompt": prompt})
        if res.status_code == 200:
            st.success(res.json()["response"])
        else:
            st.error("Error fetching response.")
