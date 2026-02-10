from risk_engine.risk_rules import HIGH_RISK, MEDIUM_RISK, LOW_RISK


from risk_engine.thresholds import SIMILARITY_THRESHOLDS, COVERAGE_THRESHOLDS

def score_obligation_risk(similarity, coverage, criticality):
    # Force HIGH risk if obligation is legally critical
    if criticality == "HIGH" and similarity < SIMILARITY_THRESHOLDS["MEDIUM"]:
        return "HIGH"

    # Similarity-based decision
    if similarity >= SIMILARITY_THRESHOLDS["LOW"]:
        sim_risk = "LOW"
    elif similarity >= SIMILARITY_THRESHOLDS["MEDIUM"]:
        sim_risk = "MEDIUM"
    else:
        sim_risk = "HIGH"

    # Coverage-based decision
    if coverage >= COVERAGE_THRESHOLDS["LOW"]:
        cov_risk = "LOW"
    elif coverage >= COVERAGE_THRESHOLDS["MEDIUM"]:
        cov_risk = "MEDIUM"
    else:
        cov_risk = "HIGH"

    # Final risk = worst case
    return max(sim_risk, cov_risk, key=lambda x: ["LOW", "MEDIUM", "HIGH"].index(x))


def overall_contract_risk(risks):
    if "HIGH" in risks:
        return "HIGH"
    if "MEDIUM" in risks:
        return "MEDIUM"
    return "LOW"

def coverage_score(sentence, required_keywords):
    if not required_keywords:
        return 1.0  # semantic obligation, no keyword coverage required

    hits = 0
    for kw in required_keywords:
        if kw.lower() in sentence.lower():
            hits += 1

    return hits / len(required_keywords)

