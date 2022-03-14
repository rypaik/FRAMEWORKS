[SOURCE](https://dev.to/nagatodev/getting-started-with-flask-1kn1)

Basic Flask App with preferences to make dev process simpler


run command: flask run



Structure
.
├── Pipfile
├── README.md
├── base.py
├── core
│   ├── __init__.py
│   ├── templates
│   │   └── index.html
│   └── views.py
└── env


init.py receives name of flask app from core __name__ -> assigns to app var

init,py assigns core as base app folder

