from flask import Flask, jsonify
from flask_restful import Api, Resource
from flasgger import Swagger

app = Flask(__name__)
api = Api(app)
swagger = Swagger(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # app.run(host='192.168.68.79', port=5000, debug=True, threaded=False)
    app.run(debug=True)

