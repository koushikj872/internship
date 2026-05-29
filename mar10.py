import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

# Sample Dataset
data = {
    'message': [
        'Win a free iPhone now',
        'Meeting at 3 PM',
        'Claim your prize today',
        'Project submission tomorrow',
        'Congratulations! You won cash',
        'Please attend the workshop'
    ],
    'label': [
        'spam',
        'ham',
        'spam',
        'ham',
        'spam',
        'ham'
    ]
}

df = pd.DataFrame(data)

# Features and Labels
X = df['message']
y = df['label']

# Split Data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Create Pipeline
model = Pipeline([
    ('tfidf', TfidfVectorizer()),
    ('classifier', MultinomialNB())
])

# Train Model
model.fit(X_train, y_train)

# Predict Test Data
predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

# Test New Message
new_message = input("Enter a message: ")

result = model.predict([new_message])

print("Prediction:", result[0].upper())