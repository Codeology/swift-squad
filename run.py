"""
VSCOdeology backend, Fall 2020
Contributors: Ashley Chu, Alicia Matsumoto
"""

from flask import Flask, send_file
from flask_restful import Resource, Api
import cluster as cl
import cv2
import numpy as np
from sklearn.cluster import KMeans

app = Flask(__name__)
api = Api(app)


# ImageApi to process image
class ImageApi(Resource):

    # User requests
    def get(self):
        return "GET passed"

    # MAIN METHOD:
    def post(self, image_file):
        img = cv2.imread(image_file) # this will probably need to be changed to be compatible

        img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        # Since the K-means algorithm we're about to do,
        # is very labour intensive, we will do it on a smaller image copy
        # This will not affect the quality of the algorithm
        pixelImage = img.reshape((img.shape[0] * img.shape[1], 3))
        # We use the sklearn K-Means algorithm to find the color histogram
        # from our small size image copy
        clt = KMeans(n_clusters=9)
        clt.fit(pixelImage)

        hist = cl.centroid_histogram(clt)
        color_data = np.array(clt.cluster_centers_, dtype=int)
        colors = cl.convert_to_hex(color_data)
        colors = np.sort(colors)[::-1]
        print(colors[1:])
        return "yay POST passed :)"


api.add_resource(ImageApi, '/endpoint')

if __name__ == '__main__':
    app.run(debug=True)