import streamlit as st


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

    st.markdown(f"""
    <div class="{ribbon_class}">
        {label}
    </div>
    """, unsafe_allow_html=True)


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

    ai_confidence = "High"

    if chunk_count > 3:

        ai_confidence = "Medium"

    st.markdown(f"""
    <div class="summary-card">

    <h3>Executive Summary</h3>

    <p>
    AI analysis detected potential application,
    downstream, validation, or infrastructure-related failures.
    </p>

    <br>

    <ul>
        <li><b>Important Errors:</b> {important_error_count}</li>
        <li><b>Stack Traces:</b> {stack_trace_count}</li>
        <li><b>Chunks Processed:</b> {chunk_count}</li>
        <li><b>AI Confidence:</b> {ai_confidence}</li>
    </ul>

    <br>

    <b>Analysis Coverage:</b>

    <ul>
        <li>Business failures</li>
        <li>Downstream/API failures</li>
        <li>HTTP issues</li>
        <li>Validation failures</li>
        <li>Recurring patterns</li>
        <li>Suggested fixes</li>
    </ul>

    </div>
    """, unsafe_allow_html=True)