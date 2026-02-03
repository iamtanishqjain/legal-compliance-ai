import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from preprocessing.pdf_to_text import extract_text_from_pdf
from preprocessing.text_cleaner import clean_text
from preprocessing.sentence_splitter import split_into_sentences
from regulation_engine.regulation_loader import load_obligations
from clause_extraction.baseline_tfidf import match_clauses
from risk_engine.risk_scorer import score_obligation_risk, overall_contract_risk

st.set_page_config(page_title="Legal Compliance Checker", layout="wide")

st.title("📄 Legal Compliance & Risk Checker")

uploaded_file = st.file_uploader("Upload a contract PDF", type=["pdf"])

if uploaded_file:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.read())

    obligations = load_obligations("data/regulations/labour_obligations.json")

    raw_text = extract_text_from_pdf("temp.pdf")
    cleaned = clean_text(raw_text)
    sentences = split_into_sentences(cleaned)

    results = match_clauses(sentences, obligations)

    st.subheader("🔍 Obligation Analysis")

    risks = []

    for r in results:
        st.markdown(f"### Obligation: {r['obligation']}")
        st.write(f"Similarity Score: `{r['score']:.2f}`")

        if r["matched_sentence"]:
            st.success(r["matched_sentence"])
        else:
            st.error("Clause not found")

        risk = score_obligation_risk(r["score"])
        risks.append(risk)

        st.write(f"**Risk Level:** {risk}")
        st.markdown("---")

    final_risk = overall_contract_risk(risks)

    st.subheader("⚠️ Final Contract Risk")
    st.write(final_risk)
