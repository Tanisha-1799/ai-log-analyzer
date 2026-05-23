import streamlit as st


def render_incident_insights(insights):

    st.markdown(
        "## Incident Intelligence"
    )

    col1, col2 = st.columns(2)

    categories = [
        key for key in insights.keys()
        if key != "Top Exceptions"
    ]

    for index, category in enumerate(categories):

        value = insights[category]

        target_col = (
            col1 if index % 2 == 0
            else col2
        )

        with target_col:

            st.info(
                f"{category}: {value}"
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
                f"- {exception} ({count})"
            )