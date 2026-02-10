def summarize_results(results):
    summary = {
        "total": 0,
        "LOW": 0,
        "MEDIUM": 0,
        "HIGH": 0,
        "manual_review": 0
    }

    for r in results:
        summary["total"] += 1
        summary[r["risk"]] += 1

        if r.get("manual_review"):
            summary["manual_review"] += 1

    return summary


def compliance_score(summary):
    """
    % of obligations that are NOT high risk
    """
    if summary["total"] == 0:
        return 0.0

    safe = summary["LOW"] + summary["MEDIUM"]
    return round((safe / summary["total"]) * 100, 2)
