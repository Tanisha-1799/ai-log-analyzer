import streamlit as st


# ---------------------------------------------------
# INCIDENT CARD
# ---------------------------------------------------

def render_insight_card(
    title,
    value,
    border_color="#4682B4"
):

    st.markdown(
        f"""
        <div style="
            padding: 1.2rem;
            border-radius: 14px;
            background: rgba(255,255,255,0.03);
            border-left: 5px solid {border_color};
            margin-bottom: 1rem;
        ">

            <div style="
                font-size: 0.95rem;
                opacity: 0.8;
                margin-bottom: 0.5rem;
            ">
                {title}
            </div>

            <div style="
                font-size: 2rem;
                font-weight: 700;
            ">
                {value}
            </div>

        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# MAIN RENDER
# ---------------------------------------------------

def render_incident_insights(insights):

    st.markdown(
        "## Incident Intelligence"
    )

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

        value = insights[category]

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

            st.markdown(
                f"""
                - **{exception}**
                  → {count} occurrences
                """
            )