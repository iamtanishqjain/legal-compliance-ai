from preprocessing.text_cleaner import clean_text
from preprocessing.sentence_splitter import split_into_sentences
from regulation_engine.regulation_loader import load_obligations
from clause_extraction.semantic_matcher import match_clauses_semantic
from risk_engine.risk_scorer import (
    score_obligation_risk,
    overall_contract_risk,
    coverage_score,
)
from risk_engine.confidence import confidence_score, needs_manual_review
from explainability.explanation_generator import explain_obligation

OBLIGATION_PATH = "data/regulations/labour_obligations.json"


def run_on_text(raw_text):
    cleaned = clean_text(raw_text)
    sentences = split_into_sentences(cleaned)
    obligations = load_obligations(OBLIGATION_PATH)

    matches = match_clauses_semantic(sentences, obligations)

    results = []
    obligation_risks = []

    for m in matches:
        similarity = m["score"]

        if m["matched_sentence"]:
            coverage = coverage_score(m["matched_sentence"], m["required_keywords"])
        else:
            coverage = 0.0

        risk = score_obligation_risk(
            similarity=similarity,
            coverage=coverage,
            criticality=m["criticality"],
        )
        confidence = confidence_score(similarity, coverage)
        review_flag = needs_manual_review(confidence, m["criticality"], risk)
        explanation = explain_obligation(m["obligation"], similarity, risk, review_flag)

        obligation_risks.append(risk)

        results.append({
            "obligation": m["obligation"],
            "similarity_score": round(similarity, 4),
            "coverage_score": round(coverage, 4),
            "confidence_score": confidence,
            "risk": risk,
            "manual_review": review_flag,
            "matched_sentence": m["matched_sentence"],
            "explanation": explanation,
        })

    final_risk = overall_contract_risk(obligation_risks)

    return results, final_risk
