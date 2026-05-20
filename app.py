import streamlit as st

from utils.sanitizer import sanitize_logs
from utils.prompt_builder import build_analysis_prompt
from services.ai_service import analyze_logs

st.set_page_config(
    page_title="AI Log Analyzer",
    layout="wide"
)

st.title("AI Log Analyzer")

uploaded_file = st.file_uploader(
    "Upload log file",
    type=["txt", "log"]
)

manual_logs = st.text_area(
    "Or paste logs directly",
    height=200
)

log_text = ""

if uploaded_file is not None:
    log_text = uploaded_file.read().decode("utf-8")

elif manual_logs:
    log_text = manual_logs

if log_text:

    st.subheader("Original Logs")

    st.text_area(
        "Logs Preview",
        log_text[:5000],
        height=250
    )

    sanitized_logs = sanitize_logs(log_text)

    st.subheader("Sanitized Logs")

    st.text_area(
        "Protected Preview",
        sanitized_logs[:5000],
        height=250
    )

    if st.button("Analyze Logs"):

        with st.spinner("AI is analyzing logs..."):

            try:

                prompt = build_analysis_prompt(
                    sanitized_logs[:12000]
                )

                result = analyze_logs(prompt)

                st.subheader("AI Analysis")
                st.markdown(result)

            except Exception as e:
                st.error(str(e))