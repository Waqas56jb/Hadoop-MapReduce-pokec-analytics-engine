import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('pokec_clean.csv')

# Plot age distribution
plt.hist(df['age'], bins=30)
plt.title("Age Distribution in Pokec Network")
plt.savefig('age_distribution.png')
plt.show()