# university-api
Demo API for interview

How I did this project:

- Install python3
```bash 
brew install python
```
  
- Virtual env
```bash
pip3 install virtualenv
virtualenv .
```

- Install Django
```bash
pip install Django==3.1.4
```

- Install postgresql driver
```bash
pip install psycopg2-binary
```

- Postgresql docker
```bash
docker run -d -p 5432:5432 --name demo-university -e POSTGRES_PASSWORD=admin postgres
```

- Create the database and user 
```bash
docker exec -it <id> /bin/sh; exit

CREATE DATABASE UNIVERSITY;
CREATE USER demo WITH ENCRYPTED PASSWORD 'demo';
GRANT ALL PRIVILEGES ON DATABASE UNIVERSITY TO demo;
ALTER USER demo CREATEDB;
```

- Setting up Django database
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'university',
        'USER': 'demo',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- Migrate
```bash
python manage.py migrate
```

- Add the app to settings
```python
INSTALLED_APPS = [
    'api.apps.ApiConfig',
    ...
]
```

- Create the migration
```bash
python manage.py makemigrations api
```
- Apply the migrations
```bash
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
  
- Install Django cors
```bash
pip install django-cors-headers
```

##### To show
- Models 
- Graphene configuration
- Unit test