import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

# Load final data
input_path = os.path.join('..', 'data', 'processed', 'pokec_final.csv')
df = pd.read_csv(input_path)

# 1. Boxplot: Completion % vs. Gender
plt.figure(figsize=(10, 6))
sns.boxplot(x='gender', y='completion_percentage', data=df)
plt_path = os.path.join('..', 'data', 'output', 'gender_vs_completion.png')
plt.savefig(plt_path)
plt.close()

# 2. Heatmap: Numerical correlations
corr = df[['age', 'completion_percentage', 'days_since_registration']].corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm')
heatmap_path = os.path.join('..', 'data', 'output', 'correlation_heatmap.png')
plt.savefig(heatmap_path)
plt.close()

print(f"Visualizations saved to {plt_path} and {heatmap_path}")