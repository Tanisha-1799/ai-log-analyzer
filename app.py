import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1",
    http_client=httpx.Client(verify=False)
)

st.title("AI Log Analyzer")

uploaded_file = st.file_uploader(
    "Upload a log file",
    type=["txt", "log"]
)

if uploaded_file is not None:

    log_text = uploaded_file.read().decode("utf-8")

    st.text_area(
        "Log Preview",
        log_text[:5000],
        height=300
    )

    if st.button("Analyze Logs"):

        with st.spinner("Analyzing logs..."):

            try:

                response = client.chat.completions.create(
                    model="deepseek/deepseek-v4-flash:free",
                    messages=[
                        {
                            "role": "user",
                            "content": f"""
                            Analyze these logs.

                            Identify:
                            - Errors
                            - Root cause
                            - Severity
                            - Suggested fix

                            Logs:
                            {log_text[:12000]}
                            """
                        }
                    ]
                )

                result = response.choices[0].message.content

                st.subheader("AI Analysis")
                st.write(result)

            except Exception as e:
                st.error(str(e))