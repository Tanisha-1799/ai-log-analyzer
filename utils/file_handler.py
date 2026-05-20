# -----------------------------------
# FILE HANDLER
# -----------------------------------

# Purpose:
# Safely process uploaded files
# for AI log analysis.

# Supported Formats:
# - TXT
# - LOG
# - DOCX

# Future Expansion:
# - PDF support
# - ZIP log bundles
# - CSV support
# - Multi-file analysis
# - Streaming large files

from utils.doc_reader import read_docx


SUPPORTED_FILE_TYPES = [
    ".txt",
    ".log",
    ".docx"
]


def extract_text_from_file(uploaded_file):

    file_name = uploaded_file.name.lower()

    try:

        # -----------------------------------
        # TXT / LOG FILES
        # -----------------------------------

        if file_name.endswith((".txt", ".log")):

            file_bytes = uploaded_file.read()

            # Primary encoding
            try:

                return file_bytes.decode("utf-8")

            # Fallback encoding
            except UnicodeDecodeError:

                return file_bytes.decode(
                    "latin-1",
                    errors="ignore"
                )

        # -----------------------------------
        # DOCX FILES
        # -----------------------------------

        elif file_name.endswith(".docx"):

            return read_docx(uploaded_file)

        # -----------------------------------
        # UNSUPPORTED FILES
        # -----------------------------------

        else:

            raise ValueError(
                f"""
Unsupported file format.

Supported formats:
{", ".join(SUPPORTED_FILE_TYPES)}
"""
            )

    except Exception as e:

        raise Exception(
            f"Error while processing uploaded file: {str(e)}"
        )