# -----------------------------------
# CENTRALIZED PROMPT BUILDER
# -----------------------------------

# Future Enhancements:
# - Multiple prompt versions
# - Provider-specific prompts
# - Structured JSON outputs
# - Multi-agent workflows
# - Security-focused prompts
# - Incident summarization prompts

def build_analysis_prompt(log_text, chunk_number=None, total_chunks=None):

    chunk_context = ""

    if chunk_number is not None and total_chunks is not None:

        chunk_context = f"""
Log Chunk Information:
- Current Chunk: {chunk_number}
- Total Chunks: {total_chunks}

Analyze this chunk independently while preserving
important technical observations.
"""

    return f"""
You are an expert:

- Site Reliability Engineer (SRE)
- Production Support Engineer
- QA Engineer
- Backend Systems Analyst

Your task is to analyze application logs carefully.

{chunk_context}

Analysis Requirements:

1. Identify critical errors
2. Identify root cause
3. Detect recurring failures
4. Assign severity level
5. Suggest fixes
6. Highlight suspicious patterns
7. Summarize important observations

Important Instructions:

- Be precise and technical
- Avoid hallucinations
- Do not invent missing logs
- Mention if logs appear incomplete
- Highlight production risks if detected
- Identify suspicious deployment patterns
- Mention if no errors are detected

Provide response in professional markdown format.

Logs:
{log_text}
"""