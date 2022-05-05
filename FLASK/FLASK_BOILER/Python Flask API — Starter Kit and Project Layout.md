# Python Flask API — Starter Kit and Project Layout

> APIs changed the way we build applications, there are countless examples of APIs in the world, and many ways to structure or set up your…

API Starter Kit
---------------

![](https://miro.medium.com/max/700/0*El3LQdEFO0VVoNI_.jpg)

APIs changed the way we build applications, there are countless examples of APIs in the world, and many ways to structure or set up your APIs. Today we will discuss how I use Python and Flask to build and document REST APIs that scale to every need.

As usual, I’m providing sample applications, for this case a starter kit for everyone to use and build upon, here is the link to the [final code](https://github.com/livecodestream/flask-api-starter-kit) we will review today.

Let’s first discuss the project dependencies, why each of them is necessary, and how it can benefit our project.

*   [flask](https://palletsprojects.com/p/flask/): Flask is a micro web framework which has a minimal footprint compared to others like django, and allows us to select which components and modules we want to integrate with it. Flask is highly reliable and performant.
*   [flasgger](https://github.com/flasgger/flasgger): It’s a module that helps us integrate swagger docs to a flask API.
*   [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/): Object serializer, ideal for parsing and dumping JSON data in and out of our API.
*   [apispec](https://apispec.readthedocs.io/en/latest/): Required for the integration between marshmallow and flasgger.

We will start discussing how the project layout looks like by taking a look into the folder structure:

project/  
    api/  
        model/  
            \_\_init\_\_.py  
            welcome.py  
        route/  
            home.py  
        schema/  
            \_\_init\_\_.py  
            welcome.py

    test/  
        route/  
            \_\_init\_\_.py  
            test\_home.py  
        \_\_init.py

    .gitignore  
    app.py  
    Pipfile  
    Pipfile.lock

I think that the folder structure is self-explanatory, but let’s look at it part by part API Module.

The API module will host our application code, from models, routes, schemas and controllers if needed (though I usually don’t create those).

*   The `models` are the data descriptor of our application, in many cases related to the database model, for example when using `sqlalchemy`, though they can be any class which represents the structure of our data.
*   The `routes` are the paths to our application (e.g. /api/home or /api/users) and it's where we will define the route logic, data retrieval, insertion, updates, etc.
*   The `schemas` are the views (serializers) for our data structures. We should have at least one schema per model. The schemas will have it's own definition as we will see later.

Route example
-------------

from http import HTTPStatus  
from flask import Blueprint  
from flasgger import swag\_from  
from api.model.welcome import WelcomeModel  
from api.schema.welcome import WelcomeSchema

home\_api = Blueprint('api', \_\_name\_\_)

@home\_api.route('/')  
@swag\_from({  
    'responses': {  
        HTTPStatus.OK.value: {  
            'description': 'Welcome to the Flask Starter Kit',  
            'schema': WelcomeSchema  
        }  
    }  
})  
def welcome():  
    """  
    1 liner about the route  
    A more detailed description of the endpoint  
    ---  
    """  
    result = WelcomeModel()  
    return WelcomeSchema().dump(result), 200

This is an example of the most basic definition for a route, let’s take a look into it line by line:

home\_api = Blueprint('api', \_\_name\_\_)

Blueprint creation, I like to separate the application in different [blueprints](https://flask.palletsprojects.com/en/1.1.x/tutorial/views/), where I provide at the beginning of the file the parent route, in this case `/api` and all the subsequent routes will be relative to this one.

@home\_api.route('/')  
@swag\_from({  
    'responses': {  
        HTTPStatus.OK.value: {  
            'description': 'Welcome to the Flask Starter Kit',  
            'schema': WelcomeSchema  
        }  
    }  
})  
def welcome():  
    """  
    1 liner about the route  
    A more detailed description of the endpoint  
    ---  
    """  
    result = WelcomeModel()  
    return WelcomeSchema().dump(result), 200

Next is the route itself, in this case we first define the route for the application, there are several ways to do this, and they are very well covered in the [flask docs](https://flask.palletsprojects.com/en/1.1.x/api/#flask.Flask.route). Right after the route definition we need to provide information for the swagger documentation. I’ve set an example where we define the response object, and the endpoint description as string literals, but there’s more you can do if you follow the [official documentation](https://github.com/flasgger/flasgger).

Then we need to place the code for our application, to eventually return an object from the API. To serialize the object we use our schemas as can be seen on the code.

Schemas
-------

The schemas are a very important part of this setup, and they are covered in detail in the [flask-marshmallow](https://flask-marshmallow.readthedocs.io/en/latest/) documentation, but in essence a schema is a class that defines the properties and relationships among models and others in so that python can serialize the objects.

Here are some sample schemas from my [blockchain code](https://github.com/adilmoujahid/blockchain-python-tutorial).

from flask\_marshmallow import Schema  
from marshmallow.fields import Nested, Str, Number  
from api.schema.transaction import TransactionSchema

class BlockSchema(Schema):  
    class Meta:  
        # Fields to expose  
        fields = \["index", "timestamp", "transactions", "nonce", "previous\_hash", "hash"\]

    index = Number()  
    nonce = Str()  
    timestamp = Number()  
    previous\_hash = Str()  
    hash = Str()  
    transactions = Nested(TransactionSchema, many=True)

from flask\_marshmallow import Schema  
from marshmallow.fields import Nested  
from api.schema.block import BlockSchema

class BlockchainSchema(Schema):  
    class Meta:  
        # Fields to expose  
        fields = \["blockchain"\]

    blockchain = Nested(BlockSchema, many=True)

As with any other application, tests are super important, and I could have an entire post discussing why. But here we will keep it simple. For tests I’m simply using [unittest](https://docs.python.org/2/library/unittest.html) module from python, and I try to build tests for each component. Here is an example for our home route:

from unittest import TestCase  
from app import create\_app

class TestWelcome(TestCase):  
    def setUp(self):  
        self.app = create\_app().test\_client()

    def test\_welcome(self):  
        """  
        Tests the route screen message  
        """  
        rv = self.app.get('/api/')

        # If we recalculate the hash on the block we should get the same result as we have stored  
        self.assertEqual({"message": 'Hello World!'}, rv.get\_json())

Finally, we need the place where we glue it all together, and we create our python API

from flask import Flask  
from flasgger import Swagger  
from api.route.home import home\_api

def create\_app():  
    app = Flask(\_\_name\_\_)

    app.config\['SWAGGER'\] = {  
        'title': 'Flask API Starter Kit',  
    }  
    swagger = Swagger(app)

    app.register\_blueprint(home\_api, url\_prefix='/api')

    return app

if \_\_name\_\_ == '\_\_main\_\_':  
    from argparse import ArgumentParser

    parser = ArgumentParser()  
    parser.add\_argument('-p', '--port', default=5000, type=int, help='port to listen on')  
    args = parser.parse\_args()  
    port = args.port

    app = create\_app()

    app.run(host='0.0.0.0', port=port)

In the file app.py we define the python flask application. Inside the `create_app` function you would need to specify your app name for the swagger configuration, each one of your blueprints, any other initialization step such as the db connection, all that would happen here, and there are good examples in the flask quick starter.

*   Check out the code from [flask-api-starter-kit](https://github.com/livecodestream/flask-api-starter-kit)
*   Install requirements `pipenv install`
*   Start the server with: `pipenv run python -m flask run`
*   Run tests: `pipenv run python -m unittest`
*   Visit [http://localhost/api](http://localhost/api) for the home api
*   Visit [http://localhost/apidocs](http://localhost/apidocs) for the swagger documentation

![](https://miro.medium.com/max/700/0*-vMGmyF6TjFbvtZN.jpg)

Swagger Doc UI Example

I hope this tutorial and project help you build your next API and as usual please let me know if you have any other ideas on twitter at [@livecodestream](https://twitter.com/livecodestream), or simply create an issue, or a PR on the [github project](https://github.com/livecodestream/flask-api-starter-kit).

Thanks for reading!


[Source](https://bajcmartinez.medium.com/python-flask-api-starter-kit-and-project-layout-2fe1da3a8107)