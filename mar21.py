import string

# List of common stopwords
stopwords = {
    "a", "an", "the", "is", "am", "are", "was", "were",
    "and", "or", "but", "in", "on", "at", "to", "for",
    "of", "with", "this", "that", "it"
}

def clean_text(text):
    # Convert to lowercase
    text = text.lower()

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    # Tokenize
    words = text.split()

    # Remove stopwords
    cleaned_words = [word for word in words if word not in stopwords]

    # Join words
    return " ".join(cleaned_words)

# User input
sentence = input("Enter a sentence: ")

# Clean text
cleaned = clean_text(sentence)

print("\nCleaned Text:")
print(cleaned)