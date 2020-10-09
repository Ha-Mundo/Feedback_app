# Feedback_app
Python Flask feedback application deployed on heroku that sends data to Postgres database and emails user

# Quick Start
```bash
# Add your DATABASE URI in app.py and your mail params in send_mail.py

# Install dependencies
pipenv shell
pipenv install

# Serve on localhost:5000
python app.py
```

## STEP BY STEP

## Create new directory 
```bash
mkdir feedback_app
```

## Create python virtual environment
```python
pip install pipenv
```

## Run python virtual environment
```python
pipenv shell
```

## Install packages
```python
pipenv install flask
pipenv install request
pipenv install psycopg2 #database adaptor in order to work with Postgres
pipenv install flask-sqlalchemy #abstract layer allows to work with db model similar to mangoose
pipenv install gunicorn #http server needed to deploy to Heroku
```

## Install python in Visual Studio Code and select python interpreter
python 3.8 feedback_app

## Create project folders and add files
static (logo.png, css.style)
template (index.html, success.html)
app.py

## Import Flask packages
render_template is used to render html file while request deal with request parameter
```python
from flask import Flask, render_template, request
```

## Initializize app.py
```python
app=Flask(__name__)
```

## Start creating route and define functions
```python
@app.route('/')
def index():
    return render_template('index.html')
```

## Run the server
```python 
if __name__ == '__main__':
    app.run() 
```

## Add debug mode to keep reloading server (only for development)
```python
if __name__ == '__main__':
    app.debug= True
    app.run()
```

## Import SQL Alchemy
```python
from flask_sqlalchemy import SQLAlchemy
```

## Install PostgreSQL on your system and create a new database

## Create a database variable to differentiate development database from production database

## Create database object 
```python 
db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200), unique=True)
    service = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, service, rating, comments):
        self.customer = customer
        self.service = service
        self.rating = rating
        self.comments = comments
```

## Run python from the terminal and create database table based from the app.py model
```bash 
 >>> from app import db
 >>> db.create_all()
 >>> exit() 
```

## Send database data to mailtrap.io account
create a new file inside the project directory send_mail.py and import packages
```python
from send_mail import send_mail 
```

## Deploy on Heroku
Create an account on heroku.com and install on your machine heroku cli
Create a new file .gitignore and initialize within the terminal a git repository:
```bash
# git init

# check heroku is installed -> heroku --version

# heroku login 

# create heroku application -> heroku create feedback_app

# create postgresql database on heroku -> heroku addons:create heroku-postgresql:hobby-dev --app feedback_app

# get heroku database url -> heroku config --app feedback_app

# paste the url inside app.py file in the app.config variable (production database)

# change dev mode to production

# create a new file -> Procfile and insert -> web: gunicorn app:app

# create a new file to tell which python version use -> runtime.txt and insert -> python-3.8.0

# create requirements.txt to include all the packages needed by the application -> pip freeze > requirements.txt

# add all to git repository: 
    # git add .
    # git commit -m 'Initial deploy'

# push local repo (git) into heroku -> heroku git:remote -a feedback_app

# push to heroku master branch -> git push heroku master

# heroku run python

# create db table
    # from app import db
    # db.create_all()
    # exit()

# LAUNCHE THE WEB APP -> heroku open
    # https://feedback_app.herokuapp.com/

# login into the remote database -> heroku pg:psql --app feedback_app
    # select * from feedback;

# Check email from mailtrap.io
```

