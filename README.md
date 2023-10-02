# Work Schedule

### To deactivate virtual environment run:

`deactivate`

### To run in development:

1. Clone repo:
   ```
   git clone https://github.com/andrew-novak/work-schedule work-schedule
   ```
2. Go to project root dir:
   ```
   cd work-schedule
   ```
3. Create your own virtual environment:
   ```
   python3 -m venv venv
   ```
4. Load virtual environment:
   ```
   source venv/bin/activate
   ```
5. Install dependiencies:
   ```
   pip install -r requirements.txt
   ```
6. Make your migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
7. Create a new superuser:
   ```
   python manage.py createsuperuser
   ```
8. Run development server:
   ```
   python manage.py runserver
   ```

### To run in production:

1. Set environment variables:
   ```
   WORK_SCHEDULE_IS_PRODUCTION
   WORK_SCHEDULE_HOST
   WORK_SCHEDULE_PORT
   WORK_SCHEDULE_DJANGO_SECRET_KEY
   WORK_SCHEDULE_DB_NAME
   WORK_SCHEDULE_DB_USER
   WORK_SCHEDULE_DB_PASSWORD
   WORK_SCHEDULE_STATIC_ROOT
   ```
   Optional:
   ```
   WORK_SCHEDULE_SUBLOCATION
   WORK_SCHEDULE_DEMO_USER_USERNAME
   WORK_SCHEDULE_DEMO_USER_PASSWORD
   ```
   > [!WARNING]  
   > Setting environment variables for a demo user will cause a `Login as demo user` button to appear on the login screen. This button allows users to log in without entering credentials, using the credentials specified in the environment variables. If you do not want this button to appear, do not provide demo user credentials in environment variables. If you desire a demo user button, consider using a staff user rather than a superuser.
2. Clone repo:
   ```
   git clone https://github.com/andrew-novak/work-schedule work-schedule
   ```
3. Go to project root dir:
   ```
   cd work-schedule
   ```
4. Create your own virtual environment:
   ```
   python3 -m venv venv
   ```
   (note you can run e.g. `python3.8` if `python3` is lower version than 3.8.x)
5. Load virtual environment:
   ```
   source venv/bin/activate
   ```
6. Install dependiencies
   ```
   pip install -r requirements.txt
   pip install -r requirements-prod-only.txt
   ```
7. Make your migrations:
   ```
   python manage.py makemigrations
   python manage.py migrate
   ```
8. Place static files in STATIC_ROOT:
   ```
   python manage.py collectstatic
   ```
9. Create a new superuser:
   ```
   python manage.py createsuperuser
   ```
10. Start:
    ```
    gunicorn config.wsgi:application -b 0.0.0.0:$WORK_SCHEDULE_PORT
    ```
