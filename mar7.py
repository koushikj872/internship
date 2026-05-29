from sklearn.neighbors import NearestNeighbors
import pandas as pd

# User ratings
data = {
    'Action': [5, 4, 1, 5],
    'Comedy': [4, 4, 2, 5],
    'SciFi': [5, 5, 1, 4]
}

users = ['UserA', 'UserB', 'UserC', 'UserD']

df = pd.DataFrame(data, index=users)

# KNN Model
knn = NearestNeighbors(n_neighbors=2, metric='euclidean')
knn.fit(df)

# Find neighbors for UserA
distances, indices = knn.kneighbors([df.loc['UserA']])

print("Nearest Neighbors for UserA:")

for i in range(1, len(indices[0])):  # Skip UserA itself
    print(users[indices[0][i]])