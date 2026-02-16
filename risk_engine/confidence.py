# risk_engine/confidence.py

def confidence_score(similarity, coverage):
    """
    Confidence is how certain we are about the decision.
    """
    return round((similarity * 0.7) + (coverage * 0.3), 2)


def needs_manual_review(confidence, criticality):
    """
    Manual review is required if:
    - Confidence is low
    - OR obligation is critical and confidence not strong
    """

    if criticality == "HIGH" and confidence < 0.6:
        return True

    if confidence < 0.4:
        return True

    return False
