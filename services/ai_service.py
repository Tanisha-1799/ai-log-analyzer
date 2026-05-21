from openai import OpenAI
import httpx
import os

from dotenv import load_dotenv

load_dotenv()

# -----------------------------------
# API CONFIGURATION
# -----------------------------------

api_key = os.getenv("OPENROUTER_API_KEY")

MODEL_NAME = "deepseek/deepseek-v4-flash:free"

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    http_client=httpx.Client(
        verify=False,
        timeout=60.0
    )
)

# -----------------------------------
# AI ANALYSIS FUNCTION
# -----------------------------------

def analyze_logs(prompt):

    try:

        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    except Exception as e:

        error_message = str(e)

        # -----------------------------------
        # RATE LIMIT HANDLING
        # -----------------------------------

        if "429" in error_message:

            return """
# AI Analysis Failed

## Rate Limit Reached

The free AI model request limit has been exceeded.

### Possible Reasons
- Too many chunk requests
- Daily free quota exhausted
- Free provider restrictions

### Suggested Fixes
- Wait for quota reset
- Reduce chunk count
- Increase chunk size
- Add delay between requests
- Add OpenRouter credits
- Switch to another model
"""

        # -----------------------------------
        # GENERAL ERROR HANDLING
        # -----------------------------------

        return f"""
# AI Analysis Failed

## Error Details

{error_message}
"""