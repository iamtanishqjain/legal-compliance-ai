from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model = SentenceTransformer("all-MiniLM-L6-v2")


def match_clauses_semantic(sentences, obligations, threshold=0.45):
    obligation_texts = [o["description"] for o in obligations]

    sentence_embeddings = model.encode(sentences)
    obligation_embeddings = model.encode(obligation_texts)

    similarity = cosine_similarity(sentence_embeddings, obligation_embeddings)

    results = []

    for i, obligation in enumerate(obligations):
        best_score = similarity[:, i].max()
        best_sentence_index = similarity[:, i].argmax()

        if best_score >= threshold:
            matched_sentence = sentences[best_sentence_index]
        else:
            matched_sentence = None

        results.append({
    "obligation": obligation["title"],
    "score": float(best_score),
    "matched_sentence": matched_sentence,
    "required_keywords": obligation.get("required_keywords", []),
    "criticality": obligation.get("criticality", "MEDIUM")
})


    return results
