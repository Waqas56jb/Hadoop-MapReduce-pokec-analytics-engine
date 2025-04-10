import pandas as pd

df = pd.read_csv('pokec_clean.csv')

# One-hot encode gender, region, eye_color
df = pd.get_dummies(df, columns=['gender', 'region', 'eye_color'])

# Save encoded data
df.to_csv('pokec_encoded.csv', index=False)
# Split hobbies into binary flags
hobbies = df['hobbies'].str.get_dummies(sep=',')
df = pd.concat([df, hobbies], axis=1)

# Save final data
df.to_csv('pokec_final.csv', index=False)