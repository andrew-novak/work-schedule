# Work Schedule

### To deactivate virtual environment:

`deactivate`

### To run in development:

1. Clone repo
2. Go to project root dir
3. Create your own virtual environment:
   `python3 -m venv venv`
4. Load virtual environment:
   `source venv/bin/activate`
5. Install dependiencies
   `pip install -r requirements.txt`
6. Make your migrations:
   `python manage.py makemigrations`
   `python manage.py migrate`
7. Create a new superuser:
   `python manage.py createsuperuser`
8. Run development server:
   `python manage.py runserver`

### To run in production:

1. Set environment variables:
   `WORK_SCHEDULE_PORT`
   `WORK_SCHEDULE_DB_NAME`
   `WORK_SCHEDULE_DB_USER`
   `WORK_SCHEDULE_DB_PASSWORD`
2. Clone repo
3. Go to project root dir
4. Create your own virtual environment:
   `python3 -m venv venv`
   (note you can run e.g. `python3.8` if `python3` is lower version than 3.8.x)
5. Load virtual environment:
   `source venv/bin/activate`
6. Install dependiencies
   `pip install -r requirements.txt`
   `pip install -r requirements-prod-only.txt`
7. Make your migrations:
   `python manage.py makemigrations`
   `python manage.py migrate`
8. Create a new superuser:
   `python manage.py createsuperuser`
9. ............
