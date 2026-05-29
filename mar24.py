from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

# Documents
documents = [
    "Machine learning helps computers learn from data",
    "Artificial intelligence and machine learning are transforming industries",
    "Deep learning is a branch of machine learning",
    "Data science combines statistics and machine learning",
    "Natural language processing enables computers to understand text"
]

# TF-IDF Vectorizer
vectorizer = TfidfVectorizer(stop_words='english')

tfidf_matrix = vectorizer.fit_transform(documents)

# Feature names
feature_names = vectorizer.get_feature_names_out()

# Convert to DataFrame
df = pd.DataFrame(tfidf_matrix.toarray(),
                  columns=feature_names)

print(df)

# Top 3 keywords per document
for i, row in df.iterrows():
    top_words = row.sort_values(ascending=False).head(3)

    print(f"\nDocument {i+1} Top Keywords:")
    for word, score in top_words.items():
        print(f"{word}: {score:.3f}")