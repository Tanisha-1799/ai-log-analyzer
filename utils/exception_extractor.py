import re

# -----------------------------------
# HIGH PRIORITY FAILURE PATTERNS
# -----------------------------------

HIGH_PRIORITY_PATTERNS = [

    # Exceptions
    r"exception",
    r"traceback",
    r"stack trace",

    # Generic failures
    r"\bfailed\b",
    r"\bfailure\b",
    r"\bfatal\b",
    r"\bcritical\b",
    r"\berror\b",

    # HTTP failures
    r"\b400\b",
    r"\b401\b",
    r"\b403\b",
    r"\b404\b",
    r"\b408\b",
    r"\b409\b",
    r"\b422\b",
    r"\b429\b",
    r"\b500\b",
    r"\b502\b",
    r"\b503\b",
    r"\b504\b",

    # Timeout / connection issues
    r"timeout",
    r"timed out",
    r"connection refused",
    r"connection reset",
    r"unable to connect",
    r"socket closed",

    # Auth / security
    r"unauthorized",
    r"forbidden",
    r"access denied",
    r"invalid token",
    r"authentication failed",

    # Database failures
    r"sql",
    r"database error",
    r"deadlock",
    r"constraint violation",

    # Business failures
    r"declined",
    r"rejected",
    r"service_barred",
    r"insufficient",
    r"transaction failed",
    r"payment failed",
    r"business error",

    # Downstream failures
    r"downstream",
    r"external service",
    r"third.party",
    r"dependency",

    # API / validation issues
    r"invalid request",
    r"bad request",
    r"missing required",
    r"validation failed",

    # Kubernetes / infra
    r"oomkilled",
    r"crashloopbackoff",
    r"pod failed",
    r"container error",

    # Network
    r"dns",
    r"host unreachable",
    r"network error"
]

# -----------------------------------
# LOW PRIORITY / NOISE PATTERNS
# -----------------------------------

LOW_PRIORITY_PATTERNS = [

    r"\bbegin\b",
    r"\bend\b",
    r"started",
    r"completed",
    r"found in cache",
    r"token found",
    r"health check",
    r"heartbeat",
    r"debug",
    r"trace"
]

# -----------------------------------
# MAIN EXTRACTION FUNCTION
# -----------------------------------

def extract_important_logs(log_text):

    important_lines = []

    seen_lines = set()

    lines = log_text.splitlines()

    for line in lines:

        line_lower = line.lower()

        # -----------------------------
        # SKIP LOW PRIORITY NOISE
        # -----------------------------

        skip_line = False

        for pattern in LOW_PRIORITY_PATTERNS:

            if re.search(pattern, line_lower):

                skip_line = True
                break

        if skip_line:
            continue

        # -----------------------------
        # DETECT IMPORTANT SIGNALS
        # -----------------------------

        for pattern in HIGH_PRIORITY_PATTERNS:

            if re.search(pattern, line_lower):

                cleaned_line = line.strip()

                # -----------------------------
                # DEDUPLICATION
                # -----------------------------

                if cleaned_line not in seen_lines:

                    important_lines.append(
                        cleaned_line
                    )

                    seen_lines.add(
                        cleaned_line
                    )

                break

    return "\n".join(important_lines)