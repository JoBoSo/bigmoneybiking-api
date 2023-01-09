### `.\venv\Scripts\activate`
Activate virtual environment

### `pip freeze > requirements.txt`
Create requirements

### `pip install -r requirements.txt`
Install required packages

### `python manage.py makemigrations`
Make model migration
... after adding bike_tours to `INSTALLED_APPS` in `settings.py`

### `python manage.py migrate`
Push migration

### `python manage.py runserver`
Run server

### `http://127.0.0.1:8000/admin/`
Access admin

### `python manage.py dumpdata > out.json`
Create copy of db