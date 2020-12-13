# university-api
Demo API

How I did this project:

- Install python3
```brew install python```
  
- Install Django
```pip3 install Django==3.1.4```
  
- Virtual env
```
pip3 install virtualenv
virtualenv .
```

- Install postgresql driver
```
pip install psycopg2-binary
```

- Postgresql docker
```
docker run -d -p 5432:5432 --name demo-university -e POSTGRES_PASSWORD=admin postgres
```

- Create database and user 
```bash
docker exec -it d36882756a0064799bb90392a144a5d7d89b5492bdb41b00dee42f3d2abca0dc /bin/sh; exit

CREATE DATABASE UNIVERSITY;
CREATE USER demo WITH ENCRYPTED PASSWORD 'demo';
GRANT ALL PRIVILEGES ON DATABASE UNIVERSITY TO demo;
```

- Setting Django database settings
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'university',
        'USER': 'demo',
        'PASSWORD': 'demo',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- Migrate
```bash
python manage.py migrate
```

- Create the models
```python
from django.db import models


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=8)
    credit = models.PositiveSmallIntegerField()


class Student(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=8)
    address = models.CharField(max_length=400)
    birth_date = models.DateField()
    student_id = code = models.CharField(max_length=8)
    courses = models.ManyToManyField(Course)
```

- Added the app to settings
```python
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

- Create the migration
```bash
python manage.py makemigrations api
```
- Apply the migrations
```bash
python manage.py sqlmigrate api 0001
python manage.py migrate
```

-create super user
```bash
python manage.py createsuperuser
```

- Install graphene
```bash
pip install graphene-django
```

- Install 
```pip install django-filter```
  
- Install 
```bash 
pip install django-cors-headers
```