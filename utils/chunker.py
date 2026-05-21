def split_logs_into_chunks(log_text, chunk_size=12000):

    chunks = []

    for index, i in enumerate(
        range(0, len(log_text), chunk_size),
        start=1
    ):

        chunk = log_text[i:i + chunk_size]

        chunks.append({
            "chunk_number": index,
            "chunk_text": chunk
        })

    return chunks