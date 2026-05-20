# -----------------------------------
# DOCX READER
# -----------------------------------

# Purpose:
# Extract text safely from Word documents.

# Future Enhancements:
# - Table extraction
# - Header/footer parsing
# - Embedded log detection
# - Multi-section support

from docx import Document


def read_docx(uploaded_file):

    try:

        document = Document(uploaded_file)

        full_text = []

        for paragraph in document.paragraphs:

            if paragraph.text.strip():

                full_text.append(paragraph.text)

        return "\n".join(full_text)

    except Exception as e:

        raise Exception(
            f"Failed to read DOCX file: {str(e)}"
        )