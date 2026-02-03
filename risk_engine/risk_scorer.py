from risk_engine.risk_rules import HIGH_RISK, MEDIUM_RISK, LOW_RISK


def score_obligation_risk(similarity_score: float) -> str:
    if similarity_score < 0.10:
        return HIGH_RISK
    elif similarity_score < 0.30:
        return MEDIUM_RISK
    else:
        return LOW_RISK


def overall_contract_risk(obligation_risks: list) -> str:
    if HIGH_RISK in obligation_risks:
        return HIGH_RISK
    elif obligation_risks.count(MEDIUM_RISK) >= 2:
        return MEDIUM_RISK
    else:
        return LOW_RISK
