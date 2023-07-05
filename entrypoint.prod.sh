#!/bin/sh

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
    python manage.py makemigrations
    python manage.py migrate --no-input
    python manage.py collectstatic --no-input

    username="admin"
    email="admin@admin.com"
    password="1234"

    python manage.py createsuperuser --username $username --email $email --noinput
    python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); user = User.objects.get(username='$username'); user.set_password('$password'); user.save()"
fi

exec "$@"