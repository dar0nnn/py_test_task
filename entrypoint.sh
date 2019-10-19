#!/bin/bash
echo "Waiting for postgres..."

while ! nc -z db 5432; do
  sleep 3
done

echo "PostgreSQL started"

# migrations
python manage.py makemigrations meeting_registation
python manage.py migrate
# superuser
python manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'test@example.com', 'test')"
# static for pretty admin
python manage.py collectstatic --no-input
echo 'SERVER RUNNING'
python manage.py runserver 0.0.0.0:8000
