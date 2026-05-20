from openai import OpenAI
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    http_client=httpx.Client(verify=False)
)

def analyze_logs(prompt):

    response = client.chat.completions.create(
        model="deepseek/deepseek-v4-flash:free",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content