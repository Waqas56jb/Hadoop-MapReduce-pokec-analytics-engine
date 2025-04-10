import pandas as pd
import os

# Load raw data
input_path = os.path.join('..', 'data', 'raw', 'soc-pokec-profiles.txt')
df = pd.read_csv(input_path, sep='\t', encoding='utf-8')

# Select required columns
cols = ['user_id', 'gender', 'age', 'region', 'completion_percentage', 
        'favourite_color', 'hobbies', 'spoken_languages', 'eye_color',
        'registration', 'last_login']
df = df[cols]

# Handle missing data
df = df.dropna(subset=['age', 'completion_percentage', 'gender', 'region'])

# Save cleaned data
output_path = os.path.join('..', 'data', 'processed', 'pokec_clean.csv')
df.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")