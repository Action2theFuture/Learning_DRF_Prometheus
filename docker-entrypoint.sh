#!/bin/bash

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

echo "Add datafolder"
mkdir data

# Start server
echo "Starting server"
gunicorn --bind 0.0.0.0:8000 drf_test.wsgi:application