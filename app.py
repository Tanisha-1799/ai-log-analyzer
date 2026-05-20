import streamlit as st

from utils.sanitizer import sanitize_logs
from utils.prompt_builder import build_analysis_prompt
from utils.file_handler import extract_text_from_file

from utils.chunker import split_logs_into_chunks
from utils.analyzer import combine_chunk_results

from services.ai_service import analyze_logs

import time


st.set_page_config(
    page_title="AI Log Analyzer",
    layout="wide"
)

# -----------------------------
# PAGE HEADER
# -----------------------------

st.title("AI Log Analyzer")

st.markdown("""
Analyze application logs using AI.

Supported inputs:
- TXT files
- LOG files
- DOCX documents
- Manual log paste
""")

# -----------------------------
# INPUT SECTION
# -----------------------------

uploaded_file = st.file_uploader(
    "Upload log file",
    type=["txt", "log", "docx"]
)

manual_logs = st.text_area(
    "Or paste logs directly",
    height=200,
    placeholder="Paste log snippets here..."
)

log_text = ""

# -----------------------------
# FILE HANDLING
# -----------------------------

if uploaded_file is not None:

    try:

        log_text = extract_text_from_file(uploaded_file)

        st.success("File loaded successfully")

    except Exception as e:

        st.error(f"Failed to read file: {str(e)}")

elif manual_logs:

    log_text = manual_logs

# -----------------------------
# LOG PREVIEW
# -----------------------------

if log_text:

    total_characters = len(log_text)
    total_lines = len(log_text.splitlines())

    st.info(
        f"""
Total Characters: {total_characters}

Total Lines: {total_lines}
"""
    )

    # -----------------------------
    # ORIGINAL LOGS
    # -----------------------------

    st.subheader("Original Logs")

    st.text_area(
        "Logs Preview",
        log_text[:5000],
        height=250
    )

    # -----------------------------
    # SANITIZATION
    # -----------------------------

    sanitized_logs = sanitize_logs(log_text)

    st.subheader("Sanitized Logs")

    st.text_area(
        "Protected Preview",
        sanitized_logs[:5000],
        height=250
    )

    # -----------------------------
    # CHUNKING INFO
    # -----------------------------

    if total_characters > 12000:

        st.warning("""
Large log file detected.

The application will analyze logs in chunks
to improve accuracy and reduce missed errors.
""")

    # -----------------------------
    # ANALYSIS BUTTON
    # -----------------------------

    if st.button("Analyze Logs"):

        with st.spinner("AI is analyzing logs..."):

            try:

                # -----------------------------
                # CHUNK CREATION
                # -----------------------------

                chunks = split_logs_into_chunks(
                    sanitized_logs
                )

                st.info(
                    f"Total Chunks Created: {len(chunks)}"
                )

                all_results = []

                progress_bar = st.progress(0)

                # -----------------------------
                # CHUNK ANALYSIS
                # -----------------------------

                for index, chunk in enumerate(chunks):

                    chunk_number = chunk["chunk_number"]

                    chunk_text = chunk["chunk_text"]

                    st.write(
                        f"""
Analyzing Chunk {chunk_number}/{len(chunks)}
"""
                    )

                    prompt = build_analysis_prompt(
                        log_text=chunk_text,
                        chunk_number=chunk_number,
                        total_chunks=len(chunks)
                    )

                    result = analyze_logs(prompt)
                    #time.sleep(2)   #for handling rate limiting part if initially using a free model

                    all_results.append({
                        "chunk_number": chunk_number,
                        "analysis": result
                    })

                    progress_bar.progress(
                        (index + 1) / len(chunks)
                    )

                # -----------------------------
                # FINAL REPORT
                # -----------------------------

                final_result = combine_chunk_results(
                    all_results
                )

                st.subheader("AI Analysis")

                st.markdown(final_result)

            except Exception as e:

                st.error(str(e))