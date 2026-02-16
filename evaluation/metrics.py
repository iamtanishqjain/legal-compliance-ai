def summarize_results(results):
    summary = {
    "total": len(results),
    "LOW": 0,
    "MEDIUM": 0,
    "HIGH": 0,
    "manual_review": 0,
    "UNKNOWN": 0
}

    for r in results:
        summary["total"] += 1
        risk_level = r.get("risk")

    if risk_level:
        summary[risk_level] += 1
    else:
        summary["UNKNOWN"] += 1

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
def risk_percentages(summary):
    total = summary["total"]
    if total == 0:
        return {}

    return {
        "LOW_percent": round((summary["LOW"] / total) * 100, 2),
        "MEDIUM_percent": round((summary["MEDIUM"] / total) * 100, 2),
        "HIGH_percent": round((summary["HIGH"] / total) * 100, 2),
    }
