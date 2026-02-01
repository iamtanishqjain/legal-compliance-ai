from preprocessing.pdf_to_text import extract_text_from_pdf
from preprocessing.text_cleaner import clean_text
from preprocessing.sentence_splitter import split_into_sentences
from regulation_engine.regulation_loader import load_obligations
from clause_extraction.baseline_tfidf import match_clauses

PDF_PATH = "data/contracts/sample_contract.pdf"
OBLIGATION_PATH = "data/regulations/labour_obligations.json"

raw_text = extract_text_from_pdf(PDF_PATH)
cleaned_text = clean_text(raw_text)
sentences = split_into_sentences(cleaned_text)

obligations = load_obligations(OBLIGATION_PATH)

results = match_clauses(sentences, obligations)

print("===== BASELINE COMPLIANCE CHECK =====\n")

for r in results:
    print(f"Obligation: {r['obligation']}")
    print(f"Score: {r['score']:.2f}")
    if r["matched_sentence"]:
        print(f"Matched sentence: {r['matched_sentence']}")
    else:
        print("Matched sentence: ❌ NOT FOUND")
    print("-" * 50)
