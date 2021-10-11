#!/bin/bash

# Collect static files
echo "Collect static files"
python3 manage.py collectstatic --no-input

# Apply database migrations
echo "Apply database migrations"
python3 manage.py migrate

echo "Add datafolder"
mkdir data

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8000 drf_test.wsgi:application