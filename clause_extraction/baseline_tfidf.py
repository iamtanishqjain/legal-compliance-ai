from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def match_clauses(sentences, obligations, threshold=0.15):
    obligation_texts = [o["description"] for o in obligations]

    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform(sentences + obligation_texts)

    sentence_vectors = vectors[:len(sentences)]
    obligation_vectors = vectors[len(sentences):]

    similarity = cosine_similarity(sentence_vectors, obligation_vectors)

    matches = []

    for i, obligation in enumerate(obligations):
        best_score = similarity[:, i].max()
        best_sentence_index = similarity[:, i].argmax()

        if best_score >= threshold:
            matches.append({
                "obligation": obligation["title"],
                "matched_sentence": sentences[best_sentence_index],
                "score": float(best_score)
            })
        else:
            matches.append({
                "obligation": obligation["title"],
                "matched_sentence": None,
                "score": float(best_score)
            })

    return matches
