import pandas as pd
import os
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Load cleaned data
input_path = os.path.join('..', 'data', 'processed', 'pokec_clean.csv')
df = pd.read_csv(input_path)

# Cluster age vs. completion %
X = df[['age', 'completion_percentage']].values
kmeans = KMeans(n_clusters=3)
df['cluster'] = kmeans.fit_predict(X)

# Save clustered data
output_data_path = os.path.join('..', 'data', 'processed', 'pokec_clustered.csv')
df.to_csv(output_data_path, index=False)

# Plot clusters
plt.scatter(df['age'], df['completion_percentage'], c=df['cluster'])
plt.xlabel('Age')
plt.ylabel('Completion %')
plot_path = os.path.join('..', 'data', 'output', 'clusters.png')
plt.savefig(plot_path)
print(f"Clustering results saved to {output_data_path} and {plot_path}")