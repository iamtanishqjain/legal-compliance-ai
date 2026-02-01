import spacy
from .text_cleaner import clean_text
from .pdf_to_text import extract_text_from_pdf


nlp = spacy.load("en_core_web_sm")

def split_into_sentences(text):
    doc = nlp(text)
    return [sent.text.strip() for sent in doc.sents if sent.text.strip()]


if __name__ == "__main__":
    pdf_path = "data/contracts/sample_contract.pdf"
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)

    sentences = split_into_sentences(cleaned_text)

    print("===== SENTENCES =====")
    for i, s in enumerate(sentences[:20]):
        print(f"{i+1}. {s}")
