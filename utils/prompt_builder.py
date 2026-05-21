# -----------------------------------
# PROMPT BUILDER
# -----------------------------------

# Purpose:
# Centralized prompt management
# for AI analysis workflows.

# Future:
# - Multiple prompt versions
# - Provider-specific prompts
# - System prompts
# - Structured output prompts
# - JSON mode support


def build_analysis_prompt(
    log_text,
    chunk_number=1,
    total_chunks=1
):

    return f"""
You are an expert:

- Site Reliability Engineer (SRE)
- Production Support Engineer
- QA Engineer
- Backend Systems Analyst

You are analyzing:

Chunk {chunk_number} of {total_chunks}

Analyze the logs carefully.

Tasks:
1. Identify critical errors
2. Identify root cause
3. Detect recurring failures
4. Assign severity level
5. Suggest fixes
6. Highlight suspicious patterns
7. Summarize key observations

Provide response in professional markdown format.

Logs:
{log_text}
"""