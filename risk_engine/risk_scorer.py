# risk_engine/risk_scorer.py

def coverage_score(sentence, required_keywords):
    """
    Measures how many required keywords appear in the matched sentence.
    Returns value between 0 and 1.
    """
    if not sentence or not required_keywords:
        return 0.0

    sentence_lower = sentence.lower()
    hits = sum(1 for kw in required_keywords if kw.lower() in sentence_lower)

    if len(required_keywords) == 0:
        return 0.0

    return hits / len(required_keywords)


# --- THRESHOLDS (You will tune these) ---
SIMILARITY_HIGH = 0.65
SIMILARITY_MEDIUM = 0.45

COVERAGE_GOOD = 0.6
COVERAGE_PARTIAL = 0.3


def score_obligation_risk(similarity, coverage, criticality):
    """
    Combines semantic similarity + keyword coverage + obligation criticality
    to determine risk level.
    """

    # Adjust similarity importance by criticality
    if criticality == "HIGH":
        similarity_weight = 0.6
        coverage_weight = 0.4
    else:
        similarity_weight = 0.7
        coverage_weight = 0.3

    combined_score = (similarity * similarity_weight) + (coverage * coverage_weight)

    # --- Risk Classification ---
    if combined_score >= 0.7:
        return "LOW"
    elif combined_score >= 0.45:
        return "MEDIUM"
    else:
        return "HIGH"


def overall_contract_risk(obligation_risks):
    """
    Determines overall contract risk.
    """
    if not obligation_risks:
        return "UNKNOWN"

    if "HIGH" in obligation_risks:
        return "HIGH"
    elif "MEDIUM" in obligation_risks:
        return "MEDIUM"
    else:
        return "LOW"
