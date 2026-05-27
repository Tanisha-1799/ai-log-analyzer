import streamlit as st
import html


# ---------------------------------------------------
# INCIDENT RIBBON
# ---------------------------------------------------

def render_incident_ribbon(
    important_error_count
):

    if important_error_count >= 20:

        ribbon_class = "incident-ribbon-high"
        label = "🔴 Critical Incident Detected"

    elif important_error_count >= 5:

        ribbon_class = "incident-ribbon-medium"
        label = "🟡 Moderate Incident Risk"

    else:

        ribbon_class = "incident-ribbon-low"
        label = "🟢 Low Incident Risk"

    ribbon_html = f"""
    <div class="{html.escape(str(ribbon_class))}">
        {html.escape(str(label))}
    </div>
    """

    st.markdown(
        ribbon_html,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# AI CONFIDENCE
# ---------------------------------------------------

def calculate_ai_confidence(
    chunk_count,
    important_error_count
):

    if chunk_count > 5:
        return "Medium"

    if important_error_count == 0:
        return "Medium"

    return "High"


# ---------------------------------------------------
# MAIN SUMMARY
# ---------------------------------------------------

def render_analysis_summary(
    important_error_count,
    stack_trace_count,
    chunk_count
):

    st.markdown(
        "## AI Incident Analysis"
    )

    render_incident_ribbon(
        important_error_count
    )

    ai_confidence = calculate_ai_confidence(
        chunk_count,
        important_error_count
    )

    summary_html = f"""
<div class="summary-card">

<h3 style="margin-top:0;margin-bottom:1rem;">
Executive Summary
</h3>

<div style="line-height:1.7;font-size:1rem;">

AI analysis identified potential application,
downstream dependency, validation,
authentication, or infrastructure-related failures
from the submitted logs.

<br><br>

<b>Analysis Metrics</b>

<ul>
<li><b>Important Errors:</b> {int(important_error_count)}</li>
<li><b>Stack Traces:</b> {int(stack_trace_count)}</li>
<li><b>Chunks Processed:</b> {int(chunk_count)}</li>
<li><b>AI Confidence:</b> {html.escape(str(ai_confidence))}</li>
</ul>

<br>

<b>Analysis Coverage</b>

<ul>
<li>Business transaction failures</li>
<li>Downstream/API failures</li>
<li>HTTP and validation issues</li>
<li>Authentication and security failures</li>
<li>Infrastructure instability</li>
<li>Recurring production patterns</li>
<li>Suggested remediation actions</li>
</ul>

</div>
</div>
"""

    st.markdown(
        summary_html,
        unsafe_allow_html=True
    )