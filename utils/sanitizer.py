import re


# ---------------------------------------------------
# MAIN SANITIZER
# ---------------------------------------------------

def sanitize_logs(log_text):

    sanitized_text = log_text

    # ---------------------------------------------------
    # EMAILS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'[\w\.-]+@[\w\.-]+\.\w+',
        '[EMAIL]',
        sanitized_text
    )

    # ---------------------------------------------------
    # IP ADDRESSES
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        '[IP_ADDRESS]',
        sanitized_text
    )

    # ---------------------------------------------------
    # UUIDS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'\b[a-f0-9]{8}-'
        r'[a-f0-9]{4}-'
        r'[a-f0-9]{4}-'
        r'[a-f0-9]{4}-'
        r'[a-f0-9]{12}\b',
        '[UUID]',
        sanitized_text,
        flags=re.IGNORECASE
    )

    # ---------------------------------------------------
    # BEARER TOKENS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'Bearer\s+[A-Za-z0-9\-_=]+\.[A-Za-z0-9\-_=]+\.[A-Za-z0-9\-_=]+',
        'Bearer [JWT_TOKEN]',
        sanitized_text,
        flags=re.IGNORECASE
    )

    # ---------------------------------------------------
    # RAW JWT TOKENS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'eyJ[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+',
        '[JWT_TOKEN]',
        sanitized_text
    )

    # ---------------------------------------------------
    # API KEYS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'(?i)(api[_-]?key\s*[:=]\s*)([A-Za-z0-9\-_\.]+)',
        r'\1[API_KEY]',
        sanitized_text
    )

    # ---------------------------------------------------
    # PASSWORDS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'(?i)(password\s*[:=]\s*)([^\s]+)',
        r'\1[PASSWORD]',
        sanitized_text
    )

    # ---------------------------------------------------
    # AUTHORIZATION HEADERS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'(?i)(authorization\s*[:=]\s*)(.+)',
        r'\1[REDACTED_AUTH]',
        sanitized_text
    )

    # ---------------------------------------------------
    # PHONE NUMBERS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'\+?\d[\d\s\-]{8,}\d',
        '[PHONE]',
        sanitized_text
    )

    # ---------------------------------------------------
    # CREDIT CARD NUMBERS
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'\b(?:\d[ -]*?){13,16}\b',
        '[CARD_NUMBER]',
        sanitized_text
    )

    # ---------------------------------------------------
    # INTERNAL HOSTNAMES
    # ---------------------------------------------------

    sanitized_text = re.sub(
        r'\b[\w\-]+\.internal\b',
        '[INTERNAL_HOST]',
        sanitized_text,
        flags=re.IGNORECASE
    )

    return sanitized_text