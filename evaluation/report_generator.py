# evaluation/report_generator.py

import json
from datetime import datetime
import os


def generate_report(results, summary, compliance_score):
    """
    Generates structured evaluation report.
    """

    report = {
        "timestamp": datetime.now().isoformat(),
        "total_obligations": summary["total"],
        "risk_distribution": {
            "LOW": summary["LOW"],
            "MEDIUM": summary["MEDIUM"],
            "HIGH": summary["HIGH"]
        },
        "manual_reviews_required": summary["manual_review"],
        "compliance_score_percent": compliance_score,
        "detailed_results": results
    }

    return report


def save_report(report):
    """
    Saves report as JSON in outputs/ folder
    """

    os.makedirs("outputs", exist_ok=True)

    filename = f"outputs/compliance_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=4)

    return filename
