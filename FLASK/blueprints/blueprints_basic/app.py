from flask import Flask

from flask import Blueprint
from bl_hello import blueprint_hello
# example_bp = Blueprint('bl_hello',__name__)


app = Flask(__name__)
app.register_blueprint(blueprint_hello)

@app.route('/')
def index():
    return "This is Basic First"

# @example_bp.route('/')
# def index():
#     return "this is from Bp decorator in app.py"
