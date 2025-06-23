import streamlit as st
import requests

def feedback_form_ui():
    st.header("📣 Citizen Feedback Form")

    name = st.text_input("Your Name")
    category = st.selectbox("Issue Category", ["Water", "Electricity", "Roads", "Sanitation", "Other"])
    message = st.text_area("Describe the Issue")

    if st.button("Submit Feedback"):
        if not name or not message:
            st.warning("Please fill all fields.")
        else:
            res = requests.post("http://localhost:8000/api/feedback", json={
                "name": name,
                "category": category,
                "message": message
            })

            if res.status_code == 200:
                st.success("✅ Feedback submitted successfully!")
            else:
                st.error("Submission failed.")
