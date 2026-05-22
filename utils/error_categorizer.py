import re


# ---------------------------------------------------
# ERROR CATEGORY PATTERNS
# ---------------------------------------------------

ERROR_CATEGORIES = {

    "HTTP/API Errors": [
        r"\b500\b",
        r"\b401\b",
        r"\b403\b",
        r"\b404\b",
        r"\b429\b",
        r"bad request",
        r"internal server error",
        r"gateway timeout",
    ],

    "Database Failures": [
        r"sql",
        r"database",
        r"jdbc",
        r"connection refused",
        r"hibernate",
        r"datasource",
    ],

    "Authentication Issues": [
        r"unauthorized",
        r"authentication",
        r"jwt",
        r"token expired",
        r"access denied",
    ],

    "Timeout Failures": [
        r"timeout",
        r"timed out",
        r"socket timeout",
    ],

    "Validation Failures": [
        r"validation",
        r"invalid",
        r"null",
        r"missing field",
        r"malformed",
    ],

    "Infrastructure Issues": [
        r"kubernetes",
        r"oom",
        r"memory",
        r"disk",
        r"cpu",
        r"pod",
    ],

    "Business Failures": [
        r"transaction failed",
        r"payment failed",
        r"service barred",
        r"order failed",
        r"retry failed",
    ]
}


# ---------------------------------------------------
# MAIN FUNCTION
# ---------------------------------------------------

def categorize_errors(log_text):

    category_counts = {}

    lower_logs = log_text.lower()

    for category, patterns in ERROR_CATEGORIES.items():

        count = 0

        for pattern in patterns:

            matches = re.findall(
                pattern,
                lower_logs
            )

            count += len(matches)

        category_counts[category] = count

    return category_counts