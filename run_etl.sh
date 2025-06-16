#!/bin/bash
echo "Starting ETL process at $(date)"

source venv/bin/activate

# Run pipeline
python3 scripts/etl_from_csv.py

echo "ETL process completed at $(date)"
