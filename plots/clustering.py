from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokec_clean.csv')

# Drop missing ages
df = df.dropna(subset=['age'])

# Normalize age
df['age_norm'] = (df['age'] - df['age'].mean()) / df['age'].std()

# K-Means Clustering
kmeans = KMeans(n_clusters=3)
df['cluster'] = kmeans.fit_predict(df[['age_norm']])

# Plot clusters
plt.scatter(df['age'], df['completion_percentage'], c=df['cluster'])
plt.xlabel('Age')
plt.ylabel('Completion %')
plt.savefig('clusters.png')
plt.show()