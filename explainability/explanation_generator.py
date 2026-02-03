from risk_engine.risk_rules import HIGH_RISK, MEDIUM_RISK, LOW_RISK


def explain_obligation(obligation: str, score: float, risk: str) -> str:
    if risk == HIGH_RISK:
        return (
            f"The obligation '{obligation}' appears to be missing or not clearly stated "
            f"in the contract (similarity score: {score:.2f})."
        )

    elif risk == MEDIUM_RISK:
        return (
            f"The obligation '{obligation}' is mentioned, but the wording is weak or vague "
            f"(similarity score: {score:.2f}). Manual review is recommended."
        )

    else:
        return (
            f"The obligation '{obligation}' is clearly addressed in the contract "
            f"(similarity score: {score:.2f})."
        )


def explain_contract(final_risk: str) -> str:
    if final_risk == HIGH_RISK:
        return (
            "The contract has critical compliance gaps. "
            "Approval is not recommended without legal review."
        )

    elif final_risk == MEDIUM_RISK:
        return (
            "The contract has moderate compliance risks. "
            "Legal clarification is advised before approval."
        )

    else:
        return (
            "The contract satisfies the required legal obligations "
            "and appears safe from a compliance perspective."
        )
