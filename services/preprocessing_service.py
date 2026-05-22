from utils.sanitizer import sanitize_logs
from utils.exception_extractor import (
    extract_important_logs
)
from utils.stacktrace_extractor import (
    extract_stack_traces
)


def preprocess_logs(log_text):

    sanitized_logs = sanitize_logs(log_text)

    important_logs = extract_important_logs(
        sanitized_logs
    )

    stack_traces = extract_stack_traces(
        sanitized_logs
    )

    return {
        "sanitized_logs": sanitized_logs,
        "important_logs": important_logs,
        "stack_traces": stack_traces
    }