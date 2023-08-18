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

python manage.py runserver 0.0.0.0:8888
