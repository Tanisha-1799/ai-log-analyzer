import streamlit as st
import html


# ---------------------------------------------------
# INCIDENT CARD
# ---------------------------------------------------

def render_insight_card(
    title,
    value,
    border_color="#4682B4"
):

    safe_title = html.escape(str(title))
    safe_value = html.escape(str(value))
    safe_border = html.escape(str(border_color))

    card_html = f"""
<div style="
    padding:1.2rem;
    border-radius:14px;
    background:rgba(255,255,255,0.03);
    border-left:5px solid {safe_border};
    margin-bottom:1rem;
">

<div style="
    font-size:0.95rem;
    opacity:0.8;
    margin-bottom:0.5rem;
">
    {safe_title}
</div>

<div style="
    font-size:2rem;
    font-weight:700;
    white-space:pre-wrap;
    word-break:break-word;
">
    {safe_value}
</div>

</div>
"""

    st.markdown(
        card_html,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# MAIN RENDER
# ---------------------------------------------------

def render_incident_insights(insights):

    st.markdown(
        "## Incident Intelligence"
    )

    if not insights:

        st.info(
            "No incident insights available."
        )

        return

    col1, col2 = st.columns(2)

    categories = [
        key for key in insights.keys()
        if key != "Top Exceptions"
    ]

    color_mapping = {
        "Database Errors": "#ff6b6b",
        "Authentication Issues": "#f39c12",
        "Validation Errors": "#9b59b6",
        "API Failures": "#3498db",
        "Timeout Issues": "#e74c3c"
    }

    for index, category in enumerate(categories):

        value = insights.get(category, 0)

        border_color = color_mapping.get(
            category,
            "#4682B4"
        )

        target_col = (
            col1 if index % 2 == 0
            else col2
        )

        with target_col:

            render_insight_card(
                title=category,
                value=value,
                border_color=border_color
            )

    # ---------------------------------------------------
    # TOP EXCEPTIONS
    # ---------------------------------------------------

    top_exceptions = insights.get(
        "Top Exceptions",
        []
    )

    if top_exceptions:

        st.markdown(
            "### Top Exceptions"
        )

        for exception, count in top_exceptions:

            safe_exception = html.escape(
                str(exception)
            )

            safe_count = html.escape(
                str(count)
            )

            st.markdown(
                f"- **{safe_exception}** → {safe_count} occurrences"
            )