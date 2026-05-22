class AnalysisResult:

    def __init__(
        self,
        summary="",
        detailed_report="",
        severity="Medium",
        chunk_count=0,
        important_error_count=0,
        stack_trace_count=0,
        technical_details=None
    ):

        self.summary = summary

        self.detailed_report = detailed_report

        self.severity = severity

        self.chunk_count = chunk_count

        self.important_error_count = important_error_count

        self.stack_trace_count = stack_trace_count

        self.technical_details = technical_details or {}