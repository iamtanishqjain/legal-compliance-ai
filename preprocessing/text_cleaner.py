import re
from pdf_to_text import extract_text_from_pdf

def clean_text(text):
    # Remove multiple newlines
    text = re.sub(r'\n+', '\n', text)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    return text.strip()


if __name__ == "__main__":
    pdf_path = "data/contracts/sample_contract.pdf"
    raw_text = extract_text_from_pdf(pdf_path)
    cleaned_text = clean_text(raw_text)

    print("===== CLEANED TEXT =====")
    print(cleaned_text)
