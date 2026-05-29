import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Sample Mall Customer Dataset
data = {
    'Annual Income': [15, 18, 20, 25, 30,
                       55, 60, 65, 70, 75,
                       85, 90, 95, 100, 105],
    'Spending Score': [20, 25, 22, 28, 30,
                        50, 55, 60, 58, 62,
                        80, 85, 88, 90, 95]
}

df = pd.DataFrame(data)

# K-Means Clustering
kmeans = KMeans(n_clusters=3, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

# Display Results
print(df)

# Visualize Clusters
plt.scatter(df['Annual Income'],
            df['Spending Score'],
            c=df['Cluster'])

plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score")
plt.title("Customer Segmentation using K-Means")
plt.show()