import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('pokec_final.csv')

# Boxplot: Completion % vs. Gender
sns.boxplot(x='gender', y='completion_percentage', data=df)
plt.savefig('gender_vs_completion.png')

# Heatmap: Numerical correlations
corr = df[['age', 'completion_percentage']].corr()
sns.heatmap(corr, annot=True)
plt.savefig('heatmap.png')