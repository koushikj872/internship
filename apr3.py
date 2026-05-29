import nltk
import string
from collections import Counter
from nltk.corpus import stopwords

# Download stopwords (run once)
nltk.download('stopwords')

def extract_keywords(text):

    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize
    words = text.split()

    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [
        word for word in words
        if word not in stop_words
    ]

    # Count frequencies
    word_freq = Counter(filtered_words)

    # Get top 5 keywords
    keywords = word_freq.most_common(5)

    return keywords

# User Input
text = input("Enter a paragraph:\n")

keywords = extract_keywords(text)

print("\nTop Keywords:")
for word, count in keywords:
    print(f"{word}: {count}")