import pandas as pd

# Load data (replace with your file path)
df = pd.read_csv('soc-pokec-profiles.txt', sep='\t', encoding='utf-8')

# Keep only needed columns (adjust based on actual columns)
df = df[['user_id', 'gender', 'age', 'region', 'completion_percentage', 'favourite_color', 'hobbies']]

# Save cleaned data
df.to_csv('pokec_clean.csv', index=False)
print("Data cleaned and saved!")