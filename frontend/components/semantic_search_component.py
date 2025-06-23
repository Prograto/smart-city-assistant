import streamlit as st
import requests

def semantic_search_ui():
    st.header("🔍 Semantic Policy Search")

    file = st.file_uploader("Upload a city policy (.txt)", type="txt")
    if file and st.button("Upload Policy"):
        res = requests.post("http://localhost:8000/api/upload-policy", files={"file": file.getvalue()})
        if res.status_code == 200:
            st.success("Policy uploaded and indexed!")
        else:
            st.error("Upload failed.")

    st.markdown("### Ask a Question")
    query = st.text_input("What do you want to know?")

    if query and st.button("Search Policy"):
        res = requests.get("http://localhost:8000/api/search-policy", params={"query": query})
        if res.status_code == 200:
            st.success("📄 Most Relevant Policy Info:")
            st.write(res.json()["result"])
        else:
            st.error("Search failed.")
