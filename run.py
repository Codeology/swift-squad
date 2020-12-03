"""
VSCOdeology backend, Fall 2020
Contributors: Ashley Chu, Alicia Matsumoto
"""

import werkzeug
from flask import Flask, send_file, request
from flask_restful import Resource, Api, reqparse
import cluster as cl
import cv2
import numpy as np
from sklearn.cluster import KMeans
import os

app = Flask(__name__)
api = Api(app)


# ImageApi to process image
class ImageApi(Resource):

    def __init__(self):
        # Create a request parser
        parser = reqparse.RequestParser()
        parser.add_argument("image", type=werkzeug.datastructures.FileStorage, location='files')
        # Sending more info in the form? simply add additional arguments, with the location being 'form'
        # parser.add_argument("other_arg", type=str, location='form')
        self.req_parser = parser


    # # User requests (for easy testing)
    # def get(self):
    #     return "GET passed"

    # MAIN METHOD:
    def post(self):
        # if you change the name 'image' in .get() here, you must also change it on the frontend:
        image_file = self.req_parser.parse_args(strict=True).get("image", None)
        if image_file:
            # Get the byte content using `.read()`
            image = image_file.read()

            np_arr = np.frombuffer(image, np.uint8)
            np_arr = np.fromstring(image, np.uint8)

            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            # Since the K-means algorithm we're about to do,
            # is very labour intensive, we will do it on a smaller image copy
            # This will not affect the quality of the algorithm
            pixelImage = img.reshape((img.shape[0] * img.shape[1], 3))
            # We use the sklearn K-Means algorithm to find the color histogram
            # from our small size image copy

            clt = KMeans(n_clusters=6)
            clt.fit(pixelImage)

            hist = cl.centroid_histogram(clt)
            color_data = np.array(clt.cluster_centers_, dtype=int)
            colors = cl.convert_to_hex(color_data)
            dict_form = {}
            print(hist)
            print(colors)
            for i in range(len(hist)):
                dict_form[hist[i]] = colors[i]
            hist = np.sort(hist)[::-1]
            print(hist)
            colors_sorted = [dict_form[hist[i]] for i in range(len(hist))]
            print(colors_sorted)
            return {"colors": [color for color in colors_sorted], "percentages": [val for val in hist]}
        else:
            return "No image sent :("


api.add_resource(ImageApi, '/endpoint')

if __name__ == '__main__':
    app.run(debug=True)