import streamlit as st
import requests

def summary_ui():
    st.header("📃 Policy Document Summarizer")
    uploaded_file = st.file_uploader("Upload a .txt or .csv file", type=["txt", "csv"])

    if uploaded_file:
        content = uploaded_file.read().decode("utf-8")
        st.text_area("Original Content", value=content, height=200)

        if st.button("Summarize"):
            res = requests.post("http://localhost:8000/api/summarize", json={"text": content})
            if res.status_code == 200:
                st.success("Summary:")
                st.write(res.json()["summary"])
            else:
                st.error("Failed to summarize.")
