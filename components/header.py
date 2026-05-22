import streamlit as st

def render_header():

    st.title("AI Log Analyzer")

    st.markdown("""
Analyze application logs using AI.

Supported inputs:
- TXT files
- LOG files
- DOCX documents
- Manual log paste
""")