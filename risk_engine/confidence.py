def confidence_score(similarity, coverage):
    """
    Confidence increases when:
    - similarity is high
    - coverage is high
    """
    return round((similarity * 0.6 + coverage * 0.4), 2)


def needs_manual_review(confidence, criticality):
    """
    Critical obligations require higher confidence.
    """
    if criticality == "HIGH":
        return confidence < 0.75
    return confidence < 0.6
