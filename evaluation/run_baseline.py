from preprocessing.pdf_to_text import extract_text_from_pdf
from preprocessing.text_cleaner import clean_text
from preprocessing.sentence_splitter import split_into_sentences
from regulation_engine.regulation_loader import load_obligations
from clause_extraction.semantic_matcher import match_clauses_semantic
from risk_engine.confidence import confidence_score, needs_manual_review

from risk_engine.risk_scorer import (
    score_obligation_risk,
    overall_contract_risk,
    coverage_score
)
from explainability.explanation_generator import (
    explain_obligation,
    explain_contract,
)



PDF_PATH = "data/contracts/sample_contract.pdf"
OBLIGATION_PATH = "data/regulations/labour_obligations.json"

raw_text = extract_text_from_pdf(PDF_PATH)
cleaned_text = clean_text(raw_text)
sentences = split_into_sentences(cleaned_text)

obligations = load_obligations(OBLIGATION_PATH)

results = match_clauses_semantic(sentences, obligations)


print("===== BASELINE COMPLIANCE CHECK =====\n")

obligation_risks = []

for r in results:
    score = r["score"]

    print(f"Obligation: {r['obligation']}")
    print(f"Similarity Score: {score:.2f}")

    if r["matched_sentence"]:
        print(f"Matched sentence: {r['matched_sentence']}")
        coverage = coverage_score(
            r["matched_sentence"],
            r["required_keywords"]
        )
    else:
        print("Matched sentence: ❌ NOT FOUND")
        coverage = 0.0

    risk = score_obligation_risk(
        similarity=score,
        coverage=coverage,
        criticality=r["criticality"]
    )

    confidence = confidence_score(score, coverage)
    review_flag = needs_manual_review(confidence, r["criticality"])

    print(f"Coverage Score: {coverage:.2f}")
    print(f"Confidence Score: {confidence}")
    print(f"Risk Level: {risk}")

    if review_flag:
        print("⚠️ Manual Review Required")

    explanation = explain_obligation(
        r["obligation"], score, risk
    )

    print(f"Explanation: {explanation}")
    print("-" * 60)

    obligation_risks.append(risk)

    print(f"Risk Level: {risk}")

    explanation = explain_obligation(
        r["obligation"],
        score,
        risk
    )

    print(f"Explanation: {explanation}")
    print("\n")


# ✅ FINAL CONTRACT RISK (ONLY ONCE)
final_risk = overall_contract_risk(obligation_risks)

print("\n===== FINAL CONTRACT RISK =====")
print(final_risk)

contract_explanation = explain_contract(final_risk)

print("\n===== CONTRACT EXPLANATION =====")
print(contract_explanation)
