# Positive and Negative Word Lists
positive_words = {
    "good", "great", "excellent", "amazing",
    "awesome", "fantastic", "wonderful",
    "best", "love", "enjoyed"
}

negative_words = {
    "bad", "worst", "boring", "awful",
    "terrible", "poor", "hate",
    "disappointing", "waste", "slow"
}

def analyze_sentiment(review):
    review = review.lower().split()

    positive_count = 0
    negative_count = 0

    for word in review:
        if word in positive_words:
            positive_count += 1
        elif word in negative_words:
            negative_count += 1

    if positive_count > negative_count:
        return "Positive"
    elif negative_count > positive_count:
        return "Negative"
    else:
        return "Neutral"

# Test Reviews
reviews = [
    "This movie was amazing and fantastic",
    "The film was boring and slow",
    "The acting was good but the story was slow",
    "An excellent movie with wonderful performances",
    "The movie was okay and average"
]

for i, review in enumerate(reviews, start=1):
    sentiment = analyze_sentiment(review)
    print(f"Review {i}: {sentiment}")