import streamlit as st


# ---------------------------------------------------
# CATEGORY CARD
# ---------------------------------------------------

def render_category_card(
    category,
    count
):

    st.markdown(f"""
    <div class="analysis-card">

        <div class="analysis-title">
            {category}
        </div>

        <h2>{count}</h2>

    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------
# MAIN ANALYTICS
# ---------------------------------------------------

def render_error_analytics(
    category_counts
):

    st.markdown(
        "## Error Analytics"
    )

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