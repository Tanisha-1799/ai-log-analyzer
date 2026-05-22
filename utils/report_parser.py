import re


def extract_section(report, section_name):

    pattern = rf"## {section_name}\s*(.*?)(?=\n## |\Z)"

    match = re.search(
        pattern,
        report,
        re.DOTALL | re.IGNORECASE
    )

    if match:

        return match.group(1).strip()

    return ""


def parse_analysis_report(report):

    return {

        "severity": extract_section(
            report,
            "Overall Severity"
        ),

        "critical_errors": extract_section(
            report,
            "Critical Errors"
        ),

        "root_cause": extract_section(
            report,
            "Root Cause Analysis"
        ),

        "suggested_fixes": extract_section(
            report,
            "Suggested Fixes"
        ),

        "suspicious_patterns": extract_section(
            report,
            "Suspicious Patterns"
        ),

        "final_summary": extract_section(
            report,
            "Final Summary"
        ),

        "recommendations": extract_section(
            report,
            "Final Recommendation"
        )
    }