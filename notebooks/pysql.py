import sqlite3
import pandas as pd

conn = sqlite3.connect('../databases/netflix project.db') # creates connection object
query = open('../SQL/netflix_movies_2015.sql', 'r').read() # opens the file in read mode and reads the entrie contents into the query variable. Selects all Movies with a release year of 2015 and beyond.
df_movies = pd.read_sql_query(query,conn) # Run the SQL query on the database and loads the result into a df called df_movies
df_movies['is_recent'] = df_movies['release_year'] >= 2020 # Create a new column with Boolean value informing whether it meets the condition
df_movies = df_movies.dropna(subset=['country','release_year']) # Drop all rows which have a null value in any of these columns
df_movies.to_csv('../outputs/netflix_movies_processed.csv',index=False)
