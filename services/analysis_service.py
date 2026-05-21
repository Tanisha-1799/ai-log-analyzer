from utils.prompt_builder import build_analysis_prompt
from utils.chunker import split_logs_into_chunks
from utils.analyzer import combine_chunk_results

from services.ai_service import analyze_logs


def run_log_analysis(
    sanitized_logs,
    important_logs,
    stack_traces,
    progress_callback=None
):

    # ----------------------------------------
    # PRIORITY INPUT SELECTION
    # ----------------------------------------

    if important_logs.strip():

        analysis_input = important_logs

    elif stack_traces.strip():

        analysis_input = stack_traces

    else:

        analysis_input = sanitized_logs

    # ----------------------------------------
    # CHUNKING
    # ----------------------------------------

    if len(analysis_input) < 12000:

        chunks = [{
            "chunk_number": 1,
            "chunk_text": analysis_input
        }]

    else:

        chunks = split_logs_into_chunks(
            analysis_input
        )

    all_results = []

    # ----------------------------------------
    # ANALYZE CHUNKS
    # ----------------------------------------

    for index, chunk in enumerate(chunks):

        chunk_number = chunk["chunk_number"]

        chunk_text = chunk["chunk_text"]

        prompt = build_analysis_prompt(
            log_text=chunk_text,
            chunk_number=chunk_number,
            total_chunks=len(chunks)
        )

        result = analyze_logs(prompt)

        all_results.append({
            "chunk_number": chunk_number,
            "analysis": result
        })

        if progress_callback:

            progress_callback(
                (index + 1) / len(chunks)
            )

    # ----------------------------------------
    # FINAL REPORT
    # ----------------------------------------

    final_result = combine_chunk_results(
        all_results
    )

    return {
        "final_result": final_result,
        "chunk_count": len(chunks)
    }