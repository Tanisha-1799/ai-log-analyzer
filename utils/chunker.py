def split_logs_into_chunks(
    log_text,
    chunk_size=12000
):

    lines = log_text.splitlines()

    chunks = []

    current_chunk = []

    current_size = 0

    chunk_number = 1

    for line in lines:

        line_size = len(line)

        # -----------------------------------
        # START NEW CHUNK
        # -----------------------------------

        if current_size + line_size > chunk_size:

            chunks.append({

                "chunk_number": chunk_number,

                "chunk_text": "\n".join(
                    current_chunk
                )
            })

            chunk_number += 1

            current_chunk = []

            current_size = 0

        current_chunk.append(line)

        current_size += line_size

    # -----------------------------------
    # FINAL CHUNK
    # -----------------------------------

    if current_chunk:

        chunks.append({

            "chunk_number": chunk_number,

            "chunk_text": "\n".join(
                current_chunk
            )
        })

    return chunks