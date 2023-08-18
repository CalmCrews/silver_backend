#!/bin/bash

python manage.py migrate --noinput

python manage.py loaddata seller.json

python manage.py loaddata product.json

python manage.py loaddata user.json

python manage.py loaddata club.json

python manage.py loaddata userclub.json

python manage.py loaddata clubproduct.json

python manage.py loaddata order.json

python manage.py loaddata review.json

python manage.py collectstatic --noinput

service cron start && python manage.py crontab add

gunicorn config.wsgi:application --bind 0.0.0.0:8888
