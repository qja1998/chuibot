#!/bin/bash
service postgresql start

. $(poetry env info --path)/bin/activate

cd app/backend
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver