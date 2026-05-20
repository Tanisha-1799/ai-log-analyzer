# -----------------------------------
# LOG CHUNKER
# -----------------------------------

# Purpose:
# Split large logs into manageable chunks
# for AI processing.

# Why Chunking Matters:
# - Prevents token overflow
# - Improves AI accuracy
# - Reduces hallucinations
# - Enables scalable analysis

# Future Enhancements:
# - Token-aware chunking
# - Smart stack-trace chunking
# - Timestamp-aware chunking
# - Semantic chunk grouping

DEFAULT_CHUNK_SIZE = 6000


def split_logs_into_chunks(
    log_text,
    chunk_size=DEFAULT_CHUNK_SIZE
):

    chunks = []

    total_length = len(log_text)

    for index, start in enumerate(
        range(0, total_length, chunk_size),
        start=1
    ):

        end = start + chunk_size

        chunk_text = log_text[start:end]

        chunk_data = {
            "chunk_number": index,
            "chunk_text": chunk_text,
            "start_position": start,
            "end_position": min(end, total_length)
        }

        chunks.append(chunk_data)

    return chunks