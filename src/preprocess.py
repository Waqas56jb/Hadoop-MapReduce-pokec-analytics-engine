import pandas as pd
from datetime import datetime

# Load data (tab-separated)
df = pd.read_csv('soc-pokec-profiles.txt', sep='\t', encoding='utf-8')

# Select required columns (adjust based on actual headers)
cols = ['user_id', 'gender', 'age', 'region', 'completion_percentage', 
        'favourite_color', 'hobbies', 'spoken_languages', 'eye_color',
        'registration', 'last_login']
df = df[cols]

# Handle missing data
df = df.dropna(subset=['age', 'completion_percentage', 'gender', 'region'])

# Save cleaned data
df.to_csv('pokec_clean.csv', index=False)
print("Data cleaned and saved!")