# Contact Tracker

Description:
Our idea is to make an app and web-based solution in which each and every person having the app has its unique ID .The basic idea of this solution is to take a precautionary measure that if a person found infected later we have list and data of all the contacts that he has made to or were near to him . When two or more people come near to each other the app links the ID of all the people and send this data to the website with the time stamp .This data is can be used by officials to trace the chain .If not connected to the internet still the app keeps the data saved locally and upload it whenever internet is available .The app runs in the background . This data on the website is available for viewing to some official persons only using the login credentials and then the official can enter the id of infected person and can get list of persons he has made contact to.
The website also provide some basic information and awareness content regarding COVID-19.

Software Requirements:
The software packages required with their version are mentioned in requirements.txt file.

Process Flow:
![img1](/static/images/process_flow.jpeg)
Data Flow Diagram:
<img src="/static/images/data_flow.jpeg" alt="" width="300" height="300">











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
