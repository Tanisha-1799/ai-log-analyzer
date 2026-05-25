import re


def parse_analysis_report(report):

    failures = []

    blocks = report.split("---")

    for block in blocks:

        block = block.strip()

        if not block:
            continue

        failure_data = {

            "failure": extract_field(
                block,
                "FAILURE"
            ),

            "service": extract_field(
                block,
                "SERVICE"
            ),

            "severity": extract_field(
                block,
                "SEVERITY"
            ),

            "root_cause": extract_field(
                block,
                "ROOT CAUSE"
            ),

            "impact": extract_field(
                block,
                "IMPACT"
            ),

            "evidence": extract_field(
                block,
                "EVIDENCE"
            ),

            "recommendation": extract_field(
                block,
                "RECOMMENDATION"
            )
        }

        # Skip empty blocks

        if failure_data["failure"]:

            failures.append(
                failure_data
            )

    return {
        "failures": failures
    }


def extract_field(
    text,
    field_name
):

    pattern = rf"{field_name}:\s*(.*?)(?=\n[A-Z ]+:|\Z)"

    match = re.search(
        pattern,
        text,
        re.DOTALL
    )

    if match:

        return match.group(1).strip()

    return ""