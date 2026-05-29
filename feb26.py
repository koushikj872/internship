# data_doctor.py

import pandas as pd

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "Alice", "David"],
    "City": ["Bangalore", "bangalore", "Mumbai", "Bangalore", "DELHI"],
    "Age": [20, 21, None, 20, 22]
})

df["Age"] = df["Age"].fillna(df["Age"].mean())
df = df.drop_duplicates()
df["City"] = df["City"].str.title()

print(df)