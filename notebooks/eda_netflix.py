import pandas as pd

# load data
df = pd.read_csv('datasets/netflix_titles.csv')

# Overview
print(df.info())
print(df['type'].value_counts())
print(df['country'].value_counts(5))

# Save a cleaned version for Tableau
df_clean = df.dropna(subset=['country','type','release_year']) # Removes the rows that contains NULL values
df_clean.to_csv('outputs/netflix_cleaned.csv', index=False)