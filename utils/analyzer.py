import re


# ---------------------------------------------------
# NOISE FILTERS
# ---------------------------------------------------

NOISE_LINES = [

    "none detected",
    "no issues found",
    "no suspicious patterns observed",
    "not applicable",
    "overall logs appear stable",
    "no actionable fixes suggested",
    "no major critical failures detected",
    "no suspicious patterns detected",
    "no clear root cause identified"
]


# ---------------------------------------------------
# SECTION EXTRACTION
# ---------------------------------------------------

SECTION_ALIASES = {

    "critical_errors": [
        "Critical Errors",
        "Failures",
        "Major Failures"
    ],

    "root_cause": [
        "Root Cause Analysis",
        "Root Cause"
    ],

    "severity": [
        "Overall Severity",
        "Severity",
        "Severity Level"
    ],

    "suggested_fixes": [
        "Suggested Fixes",
        "Fixes",
        "Recommendations"
    ],

    "suspicious_patterns": [
        "Suspicious Patterns"
    ],

    "final_summary": [
        "Final Summary",
        "Summary"
    ]
}


# ---------------------------------------------------
# FLEXIBLE SECTION EXTRACTOR
# ---------------------------------------------------

def extract_section(content, aliases):

    for section_name in aliases:

        pattern = rf"(?:#+\s*)?{section_name}\s*(.*?)(?=\n#+\s|\Z)"

        match = re.search(
            pattern,
            content,
            re.DOTALL | re.IGNORECASE
        )

        if match:

            return match.group(1).strip()

    return ""


# ---------------------------------------------------
# CLEAN + DEDUPLICATION
# ---------------------------------------------------

def clean_and_deduplicate(text):

    seen = set()

    cleaned_lines = []

    for line in text.splitlines():

        stripped = line.strip()

        if not stripped:

            continue

        lower_line = stripped.lower()

        # ---------------------------------------------------
        # REMOVE NOISE
        # ---------------------------------------------------

        if any(
            noise in lower_line
            for noise in NOISE_LINES
        ):

            continue

        # ---------------------------------------------------
        # REMOVE SEPARATORS
        # ---------------------------------------------------

        if stripped in ["---", "***"]:

            continue

        # ---------------------------------------------------
        # REMOVE DUPLICATES
        # ---------------------------------------------------

        if lower_line not in seen:

            seen.add(lower_line)

            cleaned_lines.append(stripped)

    return "\n".join(cleaned_lines)


# ---------------------------------------------------
# BULLET FORMATTER
# ---------------------------------------------------

def format_as_bullets(text):

    if not text.strip():

        return ""

    formatted = []

    for line in text.splitlines():

        stripped = line.strip()

        if not stripped:

            continue

        if stripped.startswith("-"):

            formatted.append(stripped)

        else:

            formatted.append(f"- {stripped}")

    return "\n".join(formatted)


# ---------------------------------------------------
# SEVERITY AGGREGATION
# ---------------------------------------------------

def calculate_highest_severity(text):

    severity_text = text.lower()

    if any(word in severity_text for word in [
        "critical",
        "high"
    ]):

        return "High"

    if any(word in severity_text for word in [
        "medium",
        "moderate"
    ]):

        return "Medium"

    return "Low"


# ---------------------------------------------------
# MAIN AGGREGATOR
# ---------------------------------------------------

def combine_chunk_results(all_results):

    if not all_results:

        return """
# AI Incident Analysis

No analysis results generated.
"""

    critical_errors = []
    root_causes = []
    severity_levels = []
    suggested_fixes = []
    suspicious_patterns = []
    final_summaries = []

    # ---------------------------------------------------
    # PROCESS CHUNKS
    # ---------------------------------------------------

    for result in all_results:

        analysis = result.get(
            "analysis",
            ""
        )

        if not analysis.strip():

            continue

        critical_errors.append(
            extract_section(
                analysis,
                SECTION_ALIASES[
                    "critical_errors"
                ]
            )
        )

        root_causes.append(
            extract_section(
                analysis,
                SECTION_ALIASES[
                    "root_cause"
                ]
            )
        )

        severity_levels.append(
            extract_section(
                analysis,
                SECTION_ALIASES[
                    "severity"
                ]
            )
        )

        suggested_fixes.append(
            extract_section(
                analysis,
                SECTION_ALIASES[
                    "suggested_fixes"
                ]
            )
        )

        suspicious_patterns.append(
            extract_section(
                analysis,
                SECTION_ALIASES[
                    "suspicious_patterns"
                ]
            )
        )

        final_summaries.append(
            extract_section(
                analysis,
                SECTION_ALIASES[
                    "final_summary"
                ]
            )
        )

    # ---------------------------------------------------
    # CLEAN DATA
    # ---------------------------------------------------

    critical_errors = format_as_bullets(
        clean_and_deduplicate(
            "\n".join(critical_errors)
        )
    )

    root_causes = format_as_bullets(
        clean_and_deduplicate(
            "\n".join(root_causes)
        )
    )

    suggested_fixes = format_as_bullets(
        clean_and_deduplicate(
            "\n".join(suggested_fixes)
        )
    )

    suspicious_patterns = format_as_bullets(
        clean_and_deduplicate(
            "\n".join(suspicious_patterns)
        )
    )

    final_summaries = format_as_bullets(
        clean_and_deduplicate(
            "\n".join(final_summaries)
        )
    )

    # ---------------------------------------------------
    # FINAL SEVERITY
    # ---------------------------------------------------

    final_severity = calculate_highest_severity(
        "\n".join(severity_levels)
    )

    severity_emoji = {
        "High": "🔴",
        "Medium": "🟡",
        "Low": "🟢"
    }

    severity_badge = severity_emoji.get(
        final_severity,
        "🟢"
    )

    # ---------------------------------------------------
    # FALLBACKS
    # ---------------------------------------------------

    if not critical_errors:

        critical_errors = (
            "- No major critical failures detected."
        )

    if not root_causes:

        root_causes = (
            "- No clear root cause identified."
        )

    if not suggested_fixes:

        suggested_fixes = (
            "- No actionable fixes suggested."
        )

    if not suspicious_patterns:

        suspicious_patterns = (
            "- No suspicious patterns detected."
        )

    if not final_summaries:

        final_summaries = (
            "- Overall logs appear stable."
        )

    # ---------------------------------------------------
    # FINAL REPORT
    # ---------------------------------------------------

    return f"""
# AI Incident Analysis

## Overall Severity

{severity_badge} **{final_severity} Severity Incident**

---

## Critical Errors

{critical_errors}

---

## Root Cause Analysis

{root_causes}

---

## Suggested Fixes

{suggested_fixes}

---

## Suspicious Patterns

{suspicious_patterns}

---

## Final Summary

{final_summaries}

---

## Final Recommendation

- Investigate high-severity failures first
- Prioritize downstream/API failures
- Validate external service responses
- Review recurring validation failures
- Monitor repeated business error patterns
"""