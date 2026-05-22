import streamlit as st

from utils.file_handler import (
    extract_text_from_file
)

def render_upload_section():

    uploaded_file = st.file_uploader(
        "Upload log file",
        type=["txt", "log", "docx"]
    )

    manual_logs = st.text_area(
        "Or paste logs manually",
        height=200,
        placeholder="Paste application logs here..."
    )

    # ---------------------------------------------
    # FILE INPUT
    # ---------------------------------------------

    if uploaded_file is not None:

        try:

            log_text = extract_text_from_file(
                uploaded_file
            )

            st.success(
                "File loaded successfully"
            )

            return log_text

        except Exception as e:

            st.error(
                f"Failed to read file: {str(e)}"
            )

            return ""

    # ---------------------------------------------
    # MANUAL INPUT
    # ---------------------------------------------

    if manual_logs:

        return manual_logs

    return ""