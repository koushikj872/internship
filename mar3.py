# study_hours_prediction.py

from sklearn.linear_model import LinearRegression
import numpy as np

X = np.array([[1], [2], [3], [4], [5], [6], [7], [8]])
y = np.array([35, 42, 50, 58, 65, 72, 80, 88])

model = LinearRegression()
model.fit(X, y)

hours = np.array([[9]])
predicted_marks = model.predict(hours)

print(f"Predicted marks for 9 study hours: {predicted_marks[0]:.2f}")