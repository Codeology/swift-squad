"""
VSCOdeology backend, Fall 2020
Contributors: Ashley Chu, Alicia Matsumoto
"""

from flask import Flask, send_file
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

# class Class(Resource):
    # method

# api.add_resource(class, '/endpoint')

if __name__ == '__main__':
    app.run(debug=True)