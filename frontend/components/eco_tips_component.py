import streamlit as st
import requests

def eco_tips_ui():
    st.header("♻️ Eco Tips Generator")

    topic = st.text_input("Enter a topic (e.g., plastic, solar, waste)")

    if st.button("Get Eco Tips"):
        if not topic:
            st.warning("Please enter a topic.")
        else:
            res = requests.post("http://localhost:8000/api/eco-tip", json={"topic": topic})
            if res.status_code == 200:
                st.success("🌱 Here are your eco-friendly tips:")
                st.write(res.json()["tips"])
            else:
                st.error("Failed to fetch tips.")
