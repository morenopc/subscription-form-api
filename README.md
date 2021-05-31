# Django Coding Exercise

## System

- Ubuntu 20.04.2 LTS
- Python 3.8.5
- Django 3.2.3
 - django rest framework 3.12.4
- jQuery 3.6.0


## Environment Setup

### Clone, set django new project virtual environment and run

```
$ git clone git@github.com:morenopc/subscription-form-api.git
$ cd subscription-form-api
$ python3 -m venv env
$ . env/bin/activate
(env) $ python -V
Python 3.8.5
```

#### install dependencies

```
(env) $ pip install -U pip
(env) $ pip install -r requirements.txt
```

#### create database tables and run

```
(env) $ cd subscription_form_api
(env) subscription_form_api$ python manage.py migrate
(env) subscription_form_api$ python manage.py runserver
```
[http://localhost:8000/](http://localhost:8000/)


## Run Tests
```
(env) subscription_form_api$ python manage.py test
Creating test database for alias 'default'...
System check identified no issues (0 silenced).
..
----------------------------------------------------------------------
Ran 2 tests in 0.016s

OK
Destroying test database for alias 'default'...
```

## Run API

Create new subscription
```
curl -X POST -H "Content-Type: application/json" \
-d '{"name": "moreno", "email": "moreno.pinheiro@gmail.com", "subscription_type": "free"}' \
http://localhost:8000/api/subscriptions/

{"id":1,"name":"moreno","email":"moreno.pinheiro@gmail.com","subscription_type":"free"}
```

Get list of the last 10 subscriptions
```
curl http://localhost:8000/api/subscriptions/

[{"id":1,"name":"moreno","email":"moreno.pinheiro@gmail.com","subscription_type":"free"}]
```
