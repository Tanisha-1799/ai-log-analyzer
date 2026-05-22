def calculate_metrics(
    log_text,
    important_logs,
    stack_traces
):

    total_characters = len(log_text)

    total_lines = len(
        log_text.splitlines()
    )

    important_error_count = len(
        important_logs.splitlines()
    ) if important_logs.strip() else 0

    stack_trace_count = len(
        stack_traces.split("Exception")
    ) if stack_traces.strip() else 0

    return {
        "total_characters": total_characters,
        "total_lines": total_lines,
        "important_error_count": important_error_count,
        "stack_trace_count": stack_trace_count
    }