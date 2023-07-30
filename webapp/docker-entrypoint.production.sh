#!/bin/bash

python manage.py migrate --noinput

python manage.py collectstatic --noinput

service cron start && python manage.py crontab add

gunicorn config.wsgi:application --bind 0.0.0.0:8888
