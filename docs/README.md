# Netflix Data Pipeline & Analysis

## 🎯 Overview
This project analyzes Netflix’s movie catalog from 2015 onwards, using SQL for data extraction, Python for cleaning and transformation, and Tableau for visualization.

## 🛠 Tools Used
- SQLite + SQL
- Python (Pandas, sqlite3)
- Tableau
- Bash
- Git

## 🔁 Pipeline Flow
`SQL query` → `Python transformation` → `CSV export` → `Tableau visualization`

## 📊 Key Insights
- **Top Countries:** US, India, UK dominate both pre- and post-2020.
- **Content Trends:** Peak movie releases in 2017. Significant drop in 2020–2021, likely due to COVID.
- **Top Genres:** Documentaries, Stand-Up Comedy, Dramas.
- **Genre Patterns:** Comedies and Dramas maintain strong presence across years.

### Genre Trends by Country
- 📊 US: Dominated by Drama, Comedy, Stand-Up
- 📊 UK: Documentaries lead, followed by International Movies and Drama
- 📊 India: International Movies dominate; low representation for Stand-Up


## 📂 Folder Structure
- `SQL/` → Query files  
- `notebooks/` → Python scripts (`eda_netflix.py`, `pysql.py`)  
- `outputs/` → Cleaned CSVs for Tableau  
- `datasets/` → Original datasets  
- `databases/` → SQLite DB  
- `.gitignore` → Clean repo boundaries

## 🚀 Future Enhancements
- Improve dashboard storytelling and layout
- Add time-series interactivity
- Explore genre clusters with NLP
- Move to Power BI for dashboard comparison
