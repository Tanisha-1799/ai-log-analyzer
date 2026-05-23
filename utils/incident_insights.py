import re
from collections import Counter


# ---------------------------------------------------
# PATTERNS
# ---------------------------------------------------

ERROR_PATTERNS = {
    "Database Errors": [
        r"sql",
        r"database",
        r"connection refused",
        r"deadlock",
    ],

    "API Failures": [
        r"500",
        r"502",
        r"503",
        r"504",
        r"api failure",
        r"bad gateway",
    ],

    "Authentication Issues": [
        r"unauthorized",
        r"forbidden",
        r"jwt",
        r"token expired",
        r"authentication failed",
    ],

    "Timeout Issues": [
        r"timeout",
        r"timed out",
        r"socket timeout",
    ],

    "Validation Errors": [
        r"validation failed",
        r"invalid input",
        r"schema error",
    ]
}


# ---------------------------------------------------
# INCIDENT INSIGHTS
# ---------------------------------------------------

def generate_incident_insights(log_text):

    insights = {}

    lower_logs = log_text.lower()

    for category, patterns in ERROR_PATTERNS.items():

        count = 0

        for pattern in patterns:

            matches = re.findall(
                pattern,
                lower_logs
            )

            count += len(matches)

        insights[category] = count

    # ---------------------------------------------------
    # TOP EXCEPTIONS
    # ---------------------------------------------------

    exception_patterns = re.findall(
        r"\b\w+Exception\b",
        log_text
    )

    top_exceptions = Counter(
        exception_patterns
    ).most_common(5)

    insights["Top Exceptions"] = top_exceptions

    return insights