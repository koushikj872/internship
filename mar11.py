import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample mall dataset
data = {
    'Annual Income': [15,16,17,18,19,60,62,64,65,67,85,87,88,90,92],
    'Spending Score': [39,35,40,42,38,55,58,60,62,57,82,85,88,90,86]
}

df = pd.DataFrame(data)

# Apply K-Means
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

# Display clusters
print(df)

# Plot clusters
plt.scatter(df['Annual Income'],
            df['Spending Score'],
            c=df['Cluster'])

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()