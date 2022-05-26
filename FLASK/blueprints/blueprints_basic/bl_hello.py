from flask import Blueprint

blueprint_hello = Blueprint('bl_hello', __name__)

@blueprint_hello.route('/bp')
def index():
    return "This is from Blueprint Index, Hello"




