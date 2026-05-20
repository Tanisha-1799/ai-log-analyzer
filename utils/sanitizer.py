#Remove sensitive data before AI processing
#Examples: API keys, emails, IP addresses, passwords, tokens
# Acts as a privacy engine

import re

def sanitize_logs(log_text):

    # Emails
    log_text = re.sub(
        r'[\w\.-]+@[\w\.-]+',
        '[EMAIL]',
        log_text
    )

    # IP Addresses
    log_text = re.sub(
        r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
        '[IP_ADDRESS]',
        log_text
    )

    # UUIDs
    log_text = re.sub(
        r'[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}',
        '[UUID]',
        log_text,
        flags=re.IGNORECASE
    )

    # Bearer tokens
    log_text = re.sub(
        r'Bearer\s+[A-Za-z0-9\-_\.]+',
        'Bearer [TOKEN]',
        log_text
    )

    # Phone numbers
    log_text = re.sub(
        r'\+?\d[\d\s\-]{8,}\d',
        '[PHONE]',
        log_text
    )

    return log_text