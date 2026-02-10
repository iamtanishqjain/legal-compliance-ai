from preprocessing.text_cleaner import clean_text
from preprocessing.sentence_splitter import split_into_sentences
from regulation_engine.regulation_loader import load_obligations
from clause_extraction.semantic_matcher import match_clauses_semantic

OBLIGATION_PATH = "data/regulations/labour_obligations.json"

def run_on_text(raw_text):
    cleaned = clean_text(raw_text)
    sentences = split_into_sentences(cleaned)
    obligations = load_obligations(OBLIGATION_PATH)

    results = match_clauses_semantic(sentences, obligations)

    output = {}
    for r in results:
        if r["score"] > 0.45:
            output[r["obligation"]] = "PRESENT"
        else:
            output[r["obligation"]] = "MISSING"

    return output
