#!/bin/bash
echo "Starting ETL process at $(date)"
source venv/bin/activate
python3 notebooks/eda_netflix.py
echo "ETL process completed at $(date)"
