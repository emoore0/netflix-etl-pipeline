import pandas as pd
from datetime import datetime

# load data
df = pd.read_csv('.gitignore/datasets/netflix_titles.csv')

# Clean and filter
df_clean = df.dropna(subset=['country','type','release_year']) # Drop all rows which have a null value in any of these columns
df_movies = df_clean[(df_clean['type'] == 'Movie') & (df_clean['release_year'] >= 2015)].copy() # filters the dataframe for all rows where type coulumn has Movie and for all movies released after 2015

# Select relevant columns
df_movies = df_movies[['title', 'country', 'release_year', 'listed_in']]  
df_movies.columns = ['Title', 'Country', 'Release Year', 'Genres']  # Rename the columns

df_movies['Count'] = 1 # adds a count column

# Save to outputs
df_movies.to_csv('.gitignore/outputs/netflix_movies_clean_2015.csv', index=False) # No index coulmn in data i.e no column giving every row a number
print(f"Cleaned data saved for Tableau on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

# Explode the Genres column
df_movies['Genres'] = df_movies['Genres'].str.split(', ')
df_exploded = df_movies.explode('Genres')

# Save to new output for Tableau
df_exploded.to_csv('.gitignore/outputs/netflix_movies_exploded.csv', index=False)