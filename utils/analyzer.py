import re


# ---------------------------------------------------
# NOISE FILTERS
# ---------------------------------------------------

NOISE_LINES = [
    "none detected",
    "no issues found",
    "no suspicious patterns observed",
    "not applicable",
    "no clear root cause identified",
    "overall logs appear stable",
    "no fixes suggested",
    "no major critical failures detected",
    "no suspicious patterns detected",
    "no actionable fixes suggested"
]


# ---------------------------------------------------
# HELPER
# ---------------------------------------------------

def extract_section(content, section_name):

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

        # ---------------------------------------------
        # REMOVE GENERIC / NOISE OUTPUT
        # ---------------------------------------------

        if any(
            noise in lower_line
            for noise in NOISE_LINES
        ):

            continue

        # ---------------------------------------------
        # REMOVE MARKDOWN SEPARATORS
        # ---------------------------------------------

        if stripped in ["---", "***"]:

            continue

        # ---------------------------------------------
        # DEDUPLICATION
        # ---------------------------------------------

        if lower_line not in seen:

            seen.add(lower_line)

            cleaned_lines.append(stripped)

    return "\n".join(cleaned_lines)


# ---------------------------------------------------
# SEVERITY AGGREGATION
# ---------------------------------------------------

def calculate_highest_severity(severity_text):

    text = severity_text.lower()

    if "high" in text:

        return "High"

    if "medium" in text:

        return "Medium"

    return "Low"


# ---------------------------------------------------
# FORMAT BULLETS
# ---------------------------------------------------

def format_as_bullets(text):

    if not text.strip():

        return ""

    lines = text.splitlines()

    formatted = []

    for line in lines:

        stripped = line.strip()

        if not stripped:

            continue

        if stripped.startswith("-"):

            formatted.append(stripped)

        else:

            formatted.append(f"- {stripped}")

    return "\n".join(formatted)


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
    # EXTRACT SECTIONS
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
                "Critical Errors"
            )
        )

        root_causes.append(
            extract_section(
                analysis,
                "Root Cause"
            )
        )

        severity_levels.append(
            extract_section(
                analysis,
                "Severity Level"
            )
        )

        suggested_fixes.append(
            extract_section(
                analysis,
                "Suggested Fixes"
            )
        )

        suspicious_patterns.append(
            extract_section(
                analysis,
                "Suspicious Patterns"
            )
        )

        final_summaries.append(
            extract_section(
                analysis,
                "Final Summary"
            )
        )

    # ---------------------------------------------------
    # CLEAN DATA
    # ---------------------------------------------------

    critical_errors = clean_and_deduplicate(
        "\n".join(critical_errors)
    )

    root_causes = clean_and_deduplicate(
        "\n".join(root_causes)
    )

    suggested_fixes = clean_and_deduplicate(
        "\n".join(suggested_fixes)
    )

    suspicious_patterns = clean_and_deduplicate(
        "\n".join(suspicious_patterns)
    )

    final_summaries = clean_and_deduplicate(
        "\n".join(final_summaries)
    )

    # ---------------------------------------------------
    # FORMAT OUTPUT
    # ---------------------------------------------------

    critical_errors = format_as_bullets(
        critical_errors
    )

    root_causes = format_as_bullets(
        root_causes
    )

    suggested_fixes = format_as_bullets(
        suggested_fixes
    )

    suspicious_patterns = format_as_bullets(
        suspicious_patterns
    )

    final_summaries = format_as_bullets(
        final_summaries
    )

    # ---------------------------------------------------
    # FINAL SEVERITY
    # ---------------------------------------------------

    final_severity = calculate_highest_severity(
        "\n".join(severity_levels)
    )

    # ---------------------------------------------------
    # SEVERITY BADGE
    # ---------------------------------------------------

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
    # FINAL CONSOLIDATED REPORT
    # ---------------------------------------------------

    final_report = f"""
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

    return final_report