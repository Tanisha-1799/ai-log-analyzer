import streamlit as st
import html

from utils.report_parser import (
    parse_analysis_report
)


# ---------------------------------------------------
# HELPERS
# ---------------------------------------------------

def render_severity_banner(severity):

    severity_text = str(severity).lower()

    if any(word in severity_text for word in [
        "critical",
        "high"
    ]):

        st.error(severity)

    elif any(word in severity_text for word in [
        "medium",
        "moderate"
    ]):

        st.warning(severity)

    else:

        st.success(severity)


def render_card(
    title,
    content,
    border_color="#4682B4"
):

    if not str(content).strip():

        return

    safe_title = html.escape(str(title))
    safe_content = html.escape(str(content))
    safe_border = html.escape(str(border_color))

    card_html = f"""
<div style="
    padding:1.2rem;
    border-radius:12px;
    border-left:5px solid {safe_border};
    background-color:rgba(255,255,255,0.03);
    margin-bottom:1.2rem;
">

<h3 style="
    margin-top:0;
    margin-bottom:1rem;
">
    {safe_title}
</h3>

<div style="
    line-height:1.7;
    font-size:1rem;
    white-space:pre-wrap;
    word-break:break-word;
">
    {safe_content}
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

def render_analysis_result(final_result):

    # ---------------------------------------------------
    # EMPTY RESPONSE SAFETY
    # ---------------------------------------------------

    if not str(final_result).strip():

        st.warning(
            "AI returned an empty analysis report."
        )

        return

    parsed_report = parse_analysis_report(
        final_result
    )

    st.markdown(
        "## AI Incident Analysis"
    )

    # ---------------------------------------------------
    # SEVERITY
    # ---------------------------------------------------

    severity = parsed_report.get(
        "severity",
        ""
    )

    if severity:

        render_severity_banner(
            severity
        )

    # ---------------------------------------------------
    # CRITICAL ERRORS
    # ---------------------------------------------------

    render_card(
        "Critical Errors",
        parsed_report.get(
            "critical_errors",
            ""
        ),
        "#ff6b6b"
    )

    # ---------------------------------------------------
    # ROOT CAUSE
    # ---------------------------------------------------

    render_card(
        "Root Cause Analysis",
        parsed_report.get(
            "root_cause",
            ""
        ),
        "#f39c12"
    )

    # ---------------------------------------------------
    # FIXES
    # ---------------------------------------------------

    render_card(
        "Suggested Fixes",
        parsed_report.get(
            "suggested_fixes",
            ""
        ),
        "#2ecc71"
    )

    # ---------------------------------------------------
    # SUSPICIOUS PATTERNS
    # ---------------------------------------------------

    suspicious_patterns = parsed_report.get(
        "suspicious_patterns",
        ""
    )

    if suspicious_patterns:

        with st.expander(
            "Suspicious Patterns"
        ):

            st.write(
                suspicious_patterns
            )

    # ---------------------------------------------------
    # FINAL SUMMARY
    # ---------------------------------------------------

    render_card(
        "Final Summary",
        parsed_report.get(
            "final_summary",
            ""
        ),
        "#4682B4"
    )

    # ---------------------------------------------------
    # RECOMMENDATIONS
    # ---------------------------------------------------

    recommendations = parsed_report.get(
        "recommendations",
        ""
    )

    if recommendations:

        with st.expander(
            "Final Recommendations"
        ):

            st.write(
                recommendations
            )

    # ---------------------------------------------------
    # FALLBACK RENDERING
    # ---------------------------------------------------

    if not any(parsed_report.values()):

        st.markdown("---")

        st.markdown(
            "### Raw AI Response"
        )

        st.write(final_result)