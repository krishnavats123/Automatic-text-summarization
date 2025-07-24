import spacy
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def summarize_text(text, num_sentences=3):
    doc = nlp(text)
    sentences = list(doc.sents)
    word_freq = Counter(token.text.lower() for token in doc if token.is_alpha and not token.is_stop)
    sentence_scores = [(sent, sum(word_freq[token.text.lower()] for token in sent if token.text.lower() in word_freq))
                       for sent in sentences]
    ranked = sorted(sentence_scores, key=lambda x: x[1], reverse=True)
    summary = [str(sent[0]).strip() for sent in ranked[:num_sentences]]
    return ' '.join(summary)
