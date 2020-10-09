from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)


@app.route('/')
def home():
    return 'Running!'


class HelloWorld(Resource):
    def get(self):
        return {'hello' : 'world'}  # get request to HelloWorld, which we will register as a resource, with URL '/hello'
    def post(self):
        return {'world' : 'hello'}  # post request to HelloWorld, in the test file, specify what HTTP request you are trying to make


api.add_resource(HelloWorld, '/hello')


if __name__ == '__main__':
    app.run(debug=True)
