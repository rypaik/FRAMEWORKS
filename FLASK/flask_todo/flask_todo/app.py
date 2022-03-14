from flask import Flask, request, jsonify           # import flask
from models import Schema, ToDoModel
from service import ToDoService

from loguru import logger
import logging
import sys
from pathlib import Path

app = Flask(__name__)             # create an app instance

class InterceptHandler(logging.Handler):
    def emit(self, record):
        logger_opt = logger.opt(depth=6, exception=record.exc_info)
        logger_opt.log(record.levelname, record.getMessage())

def configure_logging(flask_app: Flask):
    path = Path(flask_app.config['LOG_PATH'])
    if not path.exists():
        path.mkdir(parents=True)
    log_name = Path(path, 'sips.log')


    logging.basicConfig(handlers=[InterceptHandler(level='INFO')], level='INFO')
    logger.configure(handlers=[{"sink": sys.stderr, "level": 'INFO'}])
    logger.add(
        log_name, rotation="500 MB", encoding='utf-8', colorize=False, level='INFO'
    )



@app.route("/")                   # at the end point /
def hello():                      # call method hello
    return "Hello World!"         # which returns "hello world"

# @app.route("/<name>")              # at the end point /<name>
# def hello_name(name):              # call method hello_name
#     return "Hello "+ name          # which returns "hello + name 

@app.route("/todo", methods=["POST"])
def create_todo():
    logger.info(ToDoService().create(request.get_json()))
    return ToDoService().create(request.get_json())

if __name__ == "__main__":        # on running python app.py
    Schema()
    app.run(debug=True)                     # run the flask app

