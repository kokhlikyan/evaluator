#!/bin/sh


# Run tests
python manage.py test evaluator -v 3

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput
# Start Gunicorn
exec gunicorn app.wsgi:application -b 0.0.0.0:8000
