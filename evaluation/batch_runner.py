import os
from evaluation.run_on_text import run_on_text
from evaluation.metrics import summarize_results, compliance_score

CONTRACT_FOLDER = "data/contracts"

def run_batch():
    portfolio_results = []

    for file in os.listdir(CONTRACT_FOLDER):
        if file.endswith(".pdf"):
            print(f"\n\n====== Evaluating: {file} ======")

            file_path = os.path.join(CONTRACT_FOLDER, file)

            results, final_risk = run_on_text(file_path)

            summary = summarize_results(results)
            score = compliance_score(summary)

            portfolio_results.append({
                "contract": file,
                "risk": final_risk,
                "score": score
            })

    return portfolio_results


def portfolio_summary(portfolio_results):
    print("\n\n===== PORTFOLIO SUMMARY =====")

    high = sum(1 for c in portfolio_results if c["risk"] == "HIGH")
    medium = sum(1 for c in portfolio_results if c["risk"] == "MEDIUM")
    low = sum(1 for c in portfolio_results if c["risk"] == "LOW")

    avg_score = sum(c["score"] for c in portfolio_results) / len(portfolio_results)

    print(f"Total Contracts: {len(portfolio_results)}")
    print(f"HIGH Risk: {high}")
    print(f"MEDIUM Risk: {medium}")
    print(f"LOW Risk: {low}")
    print(f"Average Compliance Score: {avg_score:.2f}%")
