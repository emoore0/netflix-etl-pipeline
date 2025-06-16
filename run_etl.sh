#!/bin/bash
echo "Starting ETL process at $(date)"

# Activates virtual environment
source venv/bin/activate

# Run pipeline
python3 scripts/etl_sql_template.py

echo "ETL process completed at $(date)"
