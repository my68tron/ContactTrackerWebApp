# ContactTrackerWebApp

This is a Django based web app which will be used to get data from its Android based app

# How to setup

Setup your virtual environment named venv

`virtualenv venv`

Switch to your virtual environment

`source venv/bin/activate`

Install packages required

`pip install -r requirements.txt`

Migrate models of each app

```python
python manage.py makemigrations info sync
python manage.py migrate
```

Create super user for admin page

`python manage.py createsuperuser`

Run server

`python manage.py runserver`