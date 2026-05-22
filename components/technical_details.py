import streamlit as st


def render_technical_details(
    log_text,
    sanitized_logs,
    important_logs,
    stack_traces
):

    st.markdown(
        "### Technical Details"
    )

    st.caption(
        """
Expand the sections below to inspect processed logs
and extracted diagnostic information.
"""
    )

    # ---------------------------------------------------
    # ORIGINAL LOGS
    # ---------------------------------------------------

    with st.expander(
        "View Original Logs"
    ):

        st.text_area(
            "Original Logs",
            log_text[:5000],
            height=250
        )

    # ---------------------------------------------------
    # SANITIZED LOGS
    # ---------------------------------------------------

    with st.expander(
        "View Sanitized Logs"
    ):

        st.text_area(
            "Sanitized Logs",
            sanitized_logs[:5000],
            height=250
        )

    # ---------------------------------------------------
    # IMPORTANT ERRORS
    # ---------------------------------------------------

    with st.expander(
        "View Important Errors"
    ):

        st.text_area(
            "Important Errors",
            important_logs[:5000],
            height=250
        )

    # ---------------------------------------------------
    # STACK TRACES
    # ---------------------------------------------------

    with st.expander(
        "View Stack Traces"
    ):

        st.text_area(
            "Stack Traces",
            stack_traces[:5000],
            height=250
        )