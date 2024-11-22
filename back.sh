service postgresql start

. $(poetry env info --path)/bin/activate

cd chuibot/backend
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py runserver
