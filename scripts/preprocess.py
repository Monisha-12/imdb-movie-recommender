import pandas as pd
import re

stop_words = {
    'the','is','and','in','to','of','a','for','on','with','as','by','at','an',
    'this','that','from','it','its','be','are','was','were','into','their','his','her'
}

df = pd.read_csv("data/movies.csv")

def clean_text(text):
    text = str(text).lower()
    text = re.sub(r'[^a-zA-Z ]', ' ', text)
    words = text.split()
    words = [w for w in words if w not in stop_words]
    return " ".join(words)

df["Storyline"] = df["Storyline"].fillna("")
df["clean_story"] = df["Storyline"].apply(clean_text)

df = df[df["clean_story"].str.strip() != ""]
df = df[df["clean_story"].str.split().str.len() >= 8]

df.to_csv("data/processed_movies.csv", index=False)

print("processed_movies.csv created successfully")
print("Total rows after cleaning:", len(df))