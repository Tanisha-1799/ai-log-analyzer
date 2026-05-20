#Acts as a centralize prompts file
#Future:
#multiple prompt versions
#system prompts
#provider-specific prompts
#structured prompts

def build_analysis_prompt(log_text):

    return f"""
You are an expert Site Reliability Engineer (SRE),
Production Support Engineer,
QA Engineer,
and Backend Systems Analyst.

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