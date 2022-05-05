[source](https://bajcmartinez.medium.com/python-flask-api-starter-kit-and-project-layout-2fe1da3a8107)
[GH Source](https://github.com/livecodestream/flask-api-starter-kit)
credit: Juan Cruz Martinez


REQUIRED:
flask: Flask is a micro web framework which has a minimal footprint compared to others like django, and allows us to select which components and modules we want to integrate with it. Flask is highly reliable and performant.

flasgger: It’s a module that helps us integrate swagger docs to a flask API.

flask-marshmallow: Object serializer, ideal for parsing and dumping JSON data in and out of our API.

apispec: Required for the integration between marshmallow and flasgger.




Environment Set Up

    Check out the code from flask-api-starter-kit
    Install requirements pipenv install
    Start the server with: pipenv run python -m flask run
    Run tests: pipenv run python -m unittest
    Visit http://localhost/api for the home api
    Visit http://localhost/apidocs for the swagger documentation
