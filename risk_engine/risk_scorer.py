from risk_engine.risk_rules import HIGH_RISK, MEDIUM_RISK, LOW_RISK


def score_obligation_risk(similarity, coverage, criticality):
    if similarity < 0.4 or coverage < 0.3:
        base_risk = "HIGH"
    elif similarity < 0.6 or coverage < 0.6:
        base_risk = "MEDIUM"
    else:
        base_risk = "LOW"

    if criticality == "HIGH" and base_risk != "LOW":
        return "HIGH"

    return base_risk


def overall_contract_risk(obligation_risks: list) -> str:
    if HIGH_RISK in obligation_risks:
        return HIGH_RISK
    elif obligation_risks.count(MEDIUM_RISK) >= 2:
        return MEDIUM_RISK
    else:
        return LOW_RISK
def coverage_score(sentence, required_keywords):
    if not required_keywords:
        return 1.0  # semantic obligation, no keyword coverage required

    hits = 0
    for kw in required_keywords:
        if kw.lower() in sentence.lower():
            hits += 1

    return hits / len(required_keywords)

