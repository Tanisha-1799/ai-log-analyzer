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

        return f"""
AI Analysis Failed

Error:
{str(e)}
"""