# -----------------------------------
# STACK TRACE EXTRACTOR
# -----------------------------------

# Purpose:
# Extract complete stack traces
# from application logs.

# Benefits:
# - Better AI root-cause analysis
# - Preserve exception continuity
# - Improve debugging quality


import re


def extract_stack_traces(log_text):

    lines = log_text.splitlines()

    stack_traces = []

    current_trace = []

    capturing = False

    exception_pattern = re.compile(
        r'(Exception|Error|Caused by)',
        re.IGNORECASE
    )

    stack_line_pattern = re.compile(
        r'^\s+at\s+'
    )

    caused_by_pattern = re.compile(
        r'^Caused by:',
        re.IGNORECASE
    )

    for line in lines:

        # -----------------------------
        # START OF EXCEPTION
        # -----------------------------

        if exception_pattern.search(line):

            if current_trace:

                stack_traces.append(
                    "\n".join(current_trace)
                )

                current_trace = []

            capturing = True

            current_trace.append(line)

            continue

        # -----------------------------
        # STACK TRACE LINES
        # -----------------------------

        if capturing:

            if (
                stack_line_pattern.search(line)
                or caused_by_pattern.search(line)
                or line.strip() == ""
            ):

                current_trace.append(line)

            else:

                stack_traces.append(
                    "\n".join(current_trace)
                )

                current_trace = []

                capturing = False

    # -----------------------------
    # FINAL TRACE
    # -----------------------------

    if current_trace:

        stack_traces.append(
            "\n".join(current_trace)
        )

    return "\n\n".join(stack_traces)