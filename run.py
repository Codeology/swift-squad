"""
VSCOdeology backend, Fall 2020
Contributors: Ashley Chu, Alicia Matsumoto
"""
from flask import Flask, send_file
from flask_restful import Resource, Api
import cluster as cl

app = Flask(__name__)
api = Api(app)


# ImageApi to process image
class ImageApi(Resource):

    # User requests
    def get(self):
        return "GET passed"

    def post(self):
        cl.test()
        return "yay POST passed :)"


api.add_resource(ImageApi, '/endpoint')

if __name__ == '__main__':
    app.run(debug=True)