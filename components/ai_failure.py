import streamlit as st


def render_ai_failure(error_message):

    st.error(
        "AI Analysis Could Not Be Completed"
    )

    st.markdown(f"""
### Reason

{error_message}

### Suggested Actions

- Retry later
- Reduce chunk count
- Add OpenRouter credits
- Switch AI provider/model
- Add delay between chunk requests
""")