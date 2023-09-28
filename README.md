# Work Schedule

### To deactivate virtual environment:

`deactivate`

### To run in development mode:

1. Clone repo
2. Go to project root dir
3. Create your own virtual environment:
   `python3 -m venv venv`
4. Load virtual environment:
   `source venv/bin/activate`
5. Install dependiencies
   `pip install -r requirements.txt`
6. Make your migrations:
   `python3 manage.py makemigrations`
   `python3 manage.py migrate`
7. Create a new superuser:
   `python3 manage.py createsuperuser`
8. Run server in development mode:
   `python3 manage.py runserver`
