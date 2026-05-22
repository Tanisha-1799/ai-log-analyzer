from openai import OpenAI
import httpx
import os

from dotenv import load_dotenv

load_dotenv()

# ---------------------------------------------------
# API CONFIGURATION
# ---------------------------------------------------

api_key = os.getenv(
    "OPENROUTER_API_KEY"
)

MODEL_NAME = (
   "deepseek/deepseek-v4-flash:free"
   #"qwen/qwen3-next-80b-a3b-instruct:free"
)

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    http_client=httpx.Client(
        verify=False,
        timeout=60.0
    )
)

# ---------------------------------------------------
# AI ANALYSIS FUNCTION
# ---------------------------------------------------

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

        result = (
            response
            .choices[0]
            .message
            .content
        )

        # ---------------------------------------------------
        # SUCCESS RESPONSE
        # ---------------------------------------------------

        return {
            "success": True,
            "content": result
        }

    except Exception as e:

        error_message = str(e)

        lower_error = error_message.lower()

        # ---------------------------------------------------
        # RATE LIMIT
        # ---------------------------------------------------

        if (
            "429" in lower_error
            or "rate limit" in lower_error
            or "quota" in lower_error
        ):

            return {
                "success": False,
                "error_type": "rate_limit",
                "message": (
                    "Free AI model quota exceeded."
                )
            }

        # ---------------------------------------------------
        # AUTHENTICATION ERROR
        # ---------------------------------------------------

        if (
            "401" in lower_error
            or "unauthorized" in lower_error
            or "invalid api key" in lower_error
        ):

            return {
                "success": False,
                "error_type": "authentication",
                "message": (
                    "Invalid or missing OpenRouter API key."
                )
            }

        # ---------------------------------------------------
        # TIMEOUT ERROR
        # ---------------------------------------------------

        if (
            "timeout" in lower_error
            or "timed out" in lower_error
        ):

            return {
                "success": False,
                "error_type": "timeout",
                "message": (
                    "AI provider request timed out."
                )
            }

        # ---------------------------------------------------
        # GENERIC FAILURE
        # ---------------------------------------------------

        return {
            "success": False,
            "error_type": "generic",
            "message": error_message
        }