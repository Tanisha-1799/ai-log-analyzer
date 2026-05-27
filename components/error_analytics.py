import streamlit as st
import html


# ---------------------------------------------------
# CATEGORY CARD
# ---------------------------------------------------

def render_category_card(
    category,
    count
):

    safe_category = html.escape(str(category))
    safe_count = html.escape(str(count))

    card_html = f"""
<div class="analysis-card">

<div class="analysis-title">
    {safe_category}
</div>

<div class="kpi-value">
    {safe_count}
</div>

</div>
"""

    st.markdown(
        card_html,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# MAIN ANALYTICS
# ---------------------------------------------------

def render_error_analytics(
    category_counts
):

    st.markdown(
        "## Incident Intelligence"
    )

    if not category_counts:

        st.info(
            "No incident analytics available."
        )

        return

    cols = st.columns(3)

    categories = list(
        category_counts.items()
    )

    for index, (
        category,
        count
    ) in enumerate(categories):

        with cols[index % 3]:

            render_category_card(
                category,
                count
            )