import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Sample dataset
data = {
    'Area': [1000, 1200, 1500, 1800, 2000],
    'Bedrooms': [2, 2, 3, 3, 4],
    'Price': [3000000, 3500000, 4500000, 5000000, 6000000]
}

df = pd.DataFrame(data)

# Features and target
X = df[['Area', 'Bedrooms']]
y = df['Price']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# New house input
area = float(input("Enter House Area (sq ft): "))
bedrooms = int(input("Enter Number of Bedrooms: "))

# Prediction
prediction = model.predict([[area, bedrooms]])

print(f"\nPredicted House Price: ₹{prediction[0]:,.2f}")