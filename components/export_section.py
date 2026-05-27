import streamlit as st


# ---------------------------------------------------
# EXPORT BUTTON CARD
# ---------------------------------------------------

def render_export_card():

    card_html = """
<div style="
    padding:1.2rem;
    border-radius:14px;
    background:rgba(255,255,255,0.03);
    border:1px solid rgba(255,255,255,0.08);
    margin-bottom:1.2rem;
">

<h3 style="
    margin-top:0;
    margin-bottom:0.6rem;
">
    Export Incident Report
</h3>

<div style="
    opacity:0.8;
    font-size:0.95rem;
    line-height:1.6;
">
    Download AI-generated investigation reports
    for sharing, debugging, auditing,
    or incident tracking.
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

def render_export_section(
    markdown_report,
    text_report
):

    render_export_card()

    col1, col2 = st.columns(2)

    with col1:

        st.download_button(
            label="Download Markdown Report",
            data=str(markdown_report),
            file_name="incident_report.md",
            mime="text/markdown",
            use_container_width=True
        )

    with col2:

        st.download_button(
            label="Download Text Report",
            data=str(text_report),
            file_name="incident_report.txt",
            mime="text/plain",
            use_container_width=True
        )