
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

names = {"Chris": {"age": 19, "gender": "male"},
        "Matt": {"age": 22, "gender":"male"}}


class HelloWorld(Resource):
    def get(self,name):
        return names[name]

api.add_resource(HelloWorld, "/helloworld/<string:name>")
    
#    def get(self):
#        return {data:"Hello World"}
    
#    def post(self):
#        return (data: "Posted"}

#    def get(self, name, test):
#        return {"name": name, "test": test}
# api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:test>")

#api.add_resource(HelloWorld, "/helloworld")


if __name__ == '__main__':
    app.run(debug=True)

