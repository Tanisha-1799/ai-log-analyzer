#Purpose
#Result or report improve adding:
#severity visualization
#structured issue sections
#executive readability
#AI result presentation
#downloadable reports


def format_analysis_report(report):

    sections = {
        "critical": [],
        "warning": [],
        "info": [],
        "general": []
    }

    lines = report.splitlines()

    for line in lines:

        lower_line = line.lower()

        # -----------------------------------
        # CRITICAL
        # -----------------------------------

        if any(keyword in lower_line for keyword in [
            "critical",
            "high",
            "failed",
            "failure",
            "service_barred",
            "declined",
            "exception",
            "error"
        ]):

            sections["critical"].append(line)

        # -----------------------------------
        # WARNING
        # -----------------------------------

        elif any(keyword in lower_line for keyword in [
            "warning",
            "warn",
            "missing",
            "not found",
            "retry"
        ]):

            sections["warning"].append(line)

        # -----------------------------------
        # INFO
        # -----------------------------------

        elif any(keyword in lower_line for keyword in [
            "info",
            "successful",
            "completed"
        ]):

            sections["info"].append(line)

        else:

            sections["general"].append(line)

    return sections