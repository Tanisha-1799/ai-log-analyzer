import streamlit as st


def render_kpi_card(
    title,
    value
):

    html = f"""
    <div class='kpi-card'>
        <div class='kpi-title'>{str(title)}</div>
        <div class='kpi-value'>{str(value)}</div>
    </div>
    """

    st.markdown(
        html,
        unsafe_allow_html=True
    )


def render_metrics(
    total_lines,
    total_characters,
    important_error_count,
    stack_trace_count
):

    st.markdown(
        "## Log Overview"
    )

    col1, col2, col3, col4 = st.columns(4)

    with col1:

        render_kpi_card(
            "Lines",
            f"{total_lines:,}"
        )

    with col2:

        render_kpi_card(
            "Characters",
            f"{total_characters:,}"
        )

    with col3:

        render_kpi_card(
            "Important Errors",
            important_error_count
        )

    with col4:

        render_kpi_card(
            "Stack Traces",
            stack_trace_count
        )