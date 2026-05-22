import streamlit as st


def render_large_file_warning(
    total_characters
):

    if total_characters > 12000:

        st.warning("""
Large log file detected.

Logs will be analyzed in chunks to improve
AI accuracy and reduce missed failures.
""")