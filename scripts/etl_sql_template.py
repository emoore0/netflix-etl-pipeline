import sqlite3
import pandas as pd
from pathlib import Path


def run_sql_query(db_path, sql_path):
    """Connect to DB and run query from SQL file."""
    with sqlite3.connect(db_path) as conn:
        with open(sql_path, 'r') as f:
            query = f.read()
        return pd.read_sql_query(query, conn)


def clean_data(df):
    """Perform generic cleaning and processing."""
    df = df.dropna(subset=['country', 'release_year'])  # Filter missing critical info
    df['is_recent'] = df['release_year'] >= 2020        # Add simple derived column
    return df


def save_outputs(df, path):
    """Save DataFrame to CSV."""
    df.to_csv(path, index=False)
    print(f"✅ Saved cleaned data to: {path}")


if __name__ == "__main__":
    # Define paths
    db_file = Path("databases/netflix_project.db")
    sql_file = Path("SQL/netflix_movies_2015.sql")
    output_file = Path("outputs/netflix_movies_clean_template.csv")

    # Run ETL steps
    print("🔄 Running SQL query...")
    df_raw = run_sql_query(db_file, sql_file)

    print("🧹 Cleaning data...")
    df_clean = clean_data(df_raw)

    print("💾 Saving output...")
    save_outputs(df_clean, output_file)

    print("✅ ETL pipeline completed.")
