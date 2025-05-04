#!/bin/bash
# scripts/start-dev.sh
set -e

echo "Running migrations..."
python app/manage.py migrate

echo "Starting development server..."
python app/manage.py runserver 0.0.0.0:8000
