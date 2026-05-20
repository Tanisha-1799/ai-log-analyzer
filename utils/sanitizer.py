# -----------------------------------
# LOG SANITIZER
# -----------------------------------

# Purpose:
# Protect sensitive information before
# sending logs to AI providers.

# Current Protection:
# - Emails
# - IP addresses
# - UUIDs
# - Tokens
# - Phone numbers
# - Password fields
# - API keys

# Future Enhancements:
# - Configurable masking rules
# - Company-specific sanitization
# - PII detection
# - Secret scanning
# - Compliance modes (GDPR/SOC2)

import re


def sanitize_logs(log_text):

    sanitized_text = log_text

    # -----------------------------------
    # EMAILS
    # -----------------------------------

    sanitized_text = re.sub(
        r'[\w\.-]+@[\w\.-]+',
        '[EMAIL]',
        sanitized_text
    )

    # -----------------------------------
    # IP ADDRESSES
    # -----------------------------------

    sanitized_text = re.sub(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        '[IP_ADDRESS]',
        sanitized_text
    )

    # -----------------------------------
    # UUIDS
    # -----------------------------------

    sanitized_text = re.sub(
        r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}',
        '[UUID]',
        sanitized_text,
        flags=re.IGNORECASE
    )

    # -----------------------------------
    # BEARER TOKENS
    # -----------------------------------

    sanitized_text = re.sub(
        r'Bearer\s+[A-Za-z0-9\-_\.]+',
        'Bearer [TOKEN]',
        sanitized_text
    )

    # -----------------------------------
    # API KEYS
    # -----------------------------------

    sanitized_text = re.sub(
        r'(?i)(api[_-]?key\s*[:=]\s*)([A-Za-z0-9\-_]+)',
        r'\1[API_KEY]',
        sanitized_text
    )

    # -----------------------------------
    # PASSWORDS
    # -----------------------------------

    sanitized_text = re.sub(
        r'(?i)(password\s*[:=]\s*)(\S+)',
        r'\1[PASSWORD]',
        sanitized_text
    )

    # -----------------------------------
    # PHONE NUMBERS
    # -----------------------------------

    sanitized_text = re.sub(
        r'\+?\d[\d\s\-]{8,}\d',
        '[PHONE]',
        sanitized_text
    )

    return sanitized_text