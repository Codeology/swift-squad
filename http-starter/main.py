from flask import Flask, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


# an introductory get request:
class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}


# a get request with an image:
class Image(Resource):

    # user requests data from source
    def get(self):
        filename = 'sample-ims/me.png'
        return send_file(filename, mimetype='image/gif')

    # user sends data from source
    def post(self):
        print("hit image post http-starter")


api.add_resource(HelloWorld, '/hello')
api.add_resource(Image, '/image')


if __name__ == '__main__':
    app.run(debug=True)