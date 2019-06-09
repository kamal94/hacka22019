rm db.sqlite3
rm govrent/migrations/*
python3 manage.py makemigrations govrent
python3 manage.py migrate
python3 govrent/data_generator.py
echo "loading fixturse"
time python3 manage.py loaddata fixtures.json
python3 manage.py runserver
