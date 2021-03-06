[ource - Credit](https://pythonbasics.org/flask-boilerplate/)


A brief introduction here:

application: All logical codes for a project are placed here
config: the configuration file for the project
deploy: deployment related files
tests: the directory file in which the unit test code is located:
manage.py: Flask-Script run file
pylintrc: pylint standard
requirements.txt list of project dependent libraries
wsgi.py:wsgi run


So where to put the code?

Place the route code in application/controllers
place the model code in application/models.
Put the code of the initialization binding app in application/init.py.
Put the database in the config/development.py file.



TREE

├── README.md
├── application
│   ├── __init__.py
│   ├── controllers
│   │   └── __init__.py
│   ├── forms
│   │   └── __init__.py
│   ├── models
│   │   └── __init__.py
│   ├── services
│   │   └── __init__.py
│   ├── static
│   │   └── __init__.py
│   ├── templates
│   │   └── __init__.py
│   └── utils
│       └── __init__.py
├── config
│   ├── __init__.py
│   ├── default.py
│   ├── development.py
│   ├── development_sample.py
│   ├── production.py
│   ├── production_sample.py
│   └── testing.py
├── deploy
│   ├── flask_env.sh
│   ├── gunicorn.conf
│   ├── nginx.conf
│   └── supervisor.conf
├── manage.py
├── pylintrc
├── requirements.txt
├── tests
│   └── __init__.py
└── wsgi.py


## REQUIREMENTS
Flask==0.10.1
flask-mongoengine==0.7.5
Flask-Login==0.3.2
Flask-Admin==1.4.0
Flask-Redis==0.1.0
Flask-WTF==0.12



## TODO:
make a flaskenv file to start this app with flask run
add loguru module
add pytest module
add redis conf and test
pip install nginx and gunicorn and test
