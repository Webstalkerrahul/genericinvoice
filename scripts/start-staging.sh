#!/bin/bash
# scripts/start-staging.sh
set -e

echo "Running migrations..."
python app/manage.py migrate --settings=myproject.settings.staging

echo "Starting Gunicorn server..."
gunicorn --chdir app myproject.wsgi:application --bind 0.0.0.0:8000 --workers 3