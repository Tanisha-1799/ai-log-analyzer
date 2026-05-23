import streamlit as st

# ---------------------------------------------------
# COMPONENTS
# ---------------------------------------------------

from components.header import (
    render_header
)

from components.styles import (
    load_css
)

from components.upload_section import (
    render_upload_section
)

from components.metrics import (
    render_metrics
)

from components.analysis_summary import (
    render_analysis_summary
)

from components.analysis_result import (
    render_analysis_result
)

from components.technical_details import (
    render_technical_details
)

from components.ui_warnings import (
    render_large_file_warning
)

from components.ai_failure import (
    render_ai_failure
)

from components.error_analytics import (
    render_error_analytics
)

from components.incident_insights import (
    render_incident_insights
)

from components.export_section import (
    render_export_section
)

# ---------------------------------------------------
# SERVICES
# ---------------------------------------------------

from services.preprocessing_service import (
    preprocess_logs
)

from services.analysis_service import (
    run_log_analysis
)

# ---------------------------------------------------
# UTILS
# ---------------------------------------------------

from utils.metrics_helper import (
    calculate_metrics
)

from utils.error_categorizer import (
    categorize_errors
)

from utils.incident_insights import (
    generate_incident_insights
)

from utils.report_exporter import (
    generate_markdown_report,
    generate_text_report
)

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Log Analyzer",
    layout="wide"
)

# ---------------------------------------------------
# LOAD UI
# ---------------------------------------------------

load_css()

render_header()

# ---------------------------------------------------
# INPUT
# ---------------------------------------------------

log_text = render_upload_section()

# ---------------------------------------------------
# PROCESS LOGS
# ---------------------------------------------------

if log_text:

    # ---------------------------------------------------
    # PREPROCESSING
    # ---------------------------------------------------

    processed_logs = preprocess_logs(
        log_text
    )

    sanitized_logs = processed_logs[
        "sanitized_logs"
    ]

    important_logs = processed_logs[
        "important_logs"
    ]

    stack_traces = processed_logs[
        "stack_traces"
    ]

    # ---------------------------------------------------
    # METRICS
    # ---------------------------------------------------

    metrics = calculate_metrics(
        log_text=log_text,
        important_logs=important_logs,
        stack_traces=stack_traces
    )

    total_lines = metrics[
        "total_lines"
    ]

    total_characters = metrics[
        "total_characters"
    ]

    important_error_count = metrics[
        "important_error_count"
    ]

    stack_trace_count = metrics[
        "stack_trace_count"
    ]

    # ---------------------------------------------------
    # RENDER METRICS
    # ---------------------------------------------------

    render_metrics(
        total_lines=total_lines,
        total_characters=total_characters,
        important_error_count=important_error_count,
        stack_trace_count=stack_trace_count
    )

    st.divider()

    # ---------------------------------------------------
    # LARGE FILE WARNING
    # ---------------------------------------------------

    render_large_file_warning(
        total_characters
    )

    # ---------------------------------------------------
    # ANALYZE BUTTON
    # ---------------------------------------------------

    if st.button(
        "Analyze Logs",
        use_container_width=True
    ):

        with st.spinner(
            "AI is analyzing logs..."
        ):

            try:

                # ---------------------------------------------------
                # PROGRESS BAR
                # ---------------------------------------------------

                progress_bar = st.progress(0)

                # ---------------------------------------------------
                # RUN ANALYSIS
                # ---------------------------------------------------

                analysis_result = run_log_analysis(
                    sanitized_logs=sanitized_logs,
                    important_logs=important_logs,
                    stack_traces=stack_traces,
                    progress_callback=lambda progress:
                    progress_bar.progress(progress)
                )

                progress_bar.empty()

                # ---------------------------------------------------
                # HANDLE AI FAILURE
                # ---------------------------------------------------

                if not analysis_result["success"]:

                    render_ai_failure(
                        analysis_result[
                            "error"
                        ]
                    )

                # ---------------------------------------------------
                # SUCCESS FLOW
                # ---------------------------------------------------

                else:

                    final_result = analysis_result[
                        "final_result"
                    ]

                    chunk_count = analysis_result[
                        "chunk_count"
                    ]

                    st.success(
                        "Analysis completed successfully"
                    )

                    # ---------------------------------------------------
                    # ERROR ANALYTICS
                    # ---------------------------------------------------

                    category_counts = categorize_errors(
                        sanitized_logs
                    )

                    render_error_analytics(
                        category_counts
                    )

                    # ---------------------------------------------------
                    # INCIDENT INSIGHTS
                    # ---------------------------------------------------

                    incident_insights = generate_incident_insights(
                        sanitized_logs
                    )

                    render_incident_insights(
                        incident_insights
                    )

                    # ---------------------------------------------------
                    # EXECUTIVE SUMMARY
                    # ---------------------------------------------------

                    render_analysis_summary(
                        important_error_count=important_error_count,
                        stack_trace_count=stack_trace_count,
                        chunk_count=chunk_count
                    )

                    # ---------------------------------------------------
                    # FINAL AI REPORT
                    # ---------------------------------------------------

                    render_analysis_result(
                        final_result
                    )

                    # ---------------------------------------------------
                    # EXPORT REPORTS
                    # ---------------------------------------------------

                    markdown_report = (
                        generate_markdown_report(
                            final_result=final_result,
                            metrics=metrics,
                            chunk_count=chunk_count
                        )
                    )

                    text_report = (
                        generate_text_report(
                            final_result=final_result,
                            metrics=metrics,
                            chunk_count=chunk_count
                        )
                    )

                    render_export_section(
                        markdown_report=markdown_report,
                        text_report=text_report
                    )

                # ---------------------------------------------------
                # TECHNICAL DETAILS
                # ---------------------------------------------------

                render_technical_details(
                    log_text=log_text,
                    sanitized_logs=sanitized_logs,
                    important_logs=important_logs,
                    stack_traces=stack_traces
                )

            except Exception as e:

                st.error(
                    f"Unexpected Error: {str(e)}"
                )