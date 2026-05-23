import streamlit as st


def render_export_section(
    markdown_report,
    text_report
):

    st.markdown(
        "## Export Incident Report"
    )

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="Download Markdown Report",
            data=markdown_report,
            file_name="incident_report.md",
            mime="text/markdown",
            use_container_width=True
        )

    with col2:

        st.download_button(
            label="Download Text Report",
            data=text_report,
            file_name="incident_report.txt",
            mime="text/plain",
            use_container_width=True
        )