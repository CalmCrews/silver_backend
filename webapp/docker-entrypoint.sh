#!/bin/bash

python manage.py migrate --noinput

python manage.py loaddata seller.json

python manage.py loaddata product.json

python manage.py collectstatic --noinput

python manage.py runserver 0.0.0.0:8888
