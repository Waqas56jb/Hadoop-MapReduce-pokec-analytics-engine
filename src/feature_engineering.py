import pandas as pd
import os

# Load clustered data
input_path = os.path.join('..', 'data', 'processed', 'pokec_clustered.csv')
df = pd.read_csv(input_path)

# 1. One-hot encode categorical variables
df = pd.get_dummies(df, columns=['gender', 'region', 'eye_color', 'favourite_color'])

# 2. Process multi-label columns (hobbies)
hobbies_dummies = df['hobbies'].str.get_dummies(sep=',')
df = pd.concat([df, hobbies_dummies], axis=1)

# 3. Calculate days since registration
df['registration'] = pd.to_datetime(df['registration'])
df['last_login'] = pd.to_datetime(df['last_login'])
df['days_since_registration'] = (df['last_login'] - df['registration']).dt.days

# Save final dataset
output_path = os.path.join('..', 'data', 'processed', 'pokec_final.csv')
df.to_csv(output_path, index=False)
print(f"Final dataset saved to {output_path}")