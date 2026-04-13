import pandas as pd
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

stop_words = {
    'the','is','and','in','to','of','a','for','on','with','as','by','at','an',
    'this','that','from','it','its','be','are','was','were','into','their','his','her'
}

df = pd.read_csv("data/processed_movies.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

tfidf = TfidfVectorizer(ngram_range=(1, 2), min_df=2, max_df=0.85)
matrix = tfidf.fit_transform(df["clean_story"])

def recommend_movie(input_text):
    cleaned_input = clean_text(input_text)
    input_vec = tfidf.transform([cleaned_input])
    scores = cosine_similarity(input_vec, matrix)[0]

    top_indices = [i for i in scores.argsort()[::-1] if scores[i] > 0.08][:5]

    if not top_indices:
        return pd.DataFrame(columns=["Movie Name", "Storyline", "Similarity Score"])

    results = df.iloc[top_indices][["Movie Name", "Storyline"]].copy()
    results["Similarity Score"] = scores[top_indices]
    return results