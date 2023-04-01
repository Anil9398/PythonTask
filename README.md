# PythonTask

In this task we need to install one package pip install django djangorestframework django-filter
After that do py manage.py makemigrations and py manage.py migrate commands
Then run the server use this command in terminal py manage.py runserver
open any browser and run this url in search bar http://127.0.0.1:8000/addresses/ here we can create, update and delete addresses
If we want a specific address to display means run this url in search bar http://127.0.0.1:8000/addresses/<id> in output will get in JSON formate
    {
        "id": 1,
        "address": "Bangalore",
        "latitude": 13547.453,
        "longitude": 64542.63
    },
