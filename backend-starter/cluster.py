import cv2
import numpy as np
from sklearn.cluster import KMeans

"""
This starter code will grab six prominent colors from an image and return them,
along with a histogram that might (need to research) contain information about
color frequencies relative to one another. 

Where to go from here:
Consider removing lightest / darkest colors
Address contrast/color similarity/other palette aesthetics 
Create metric to measure color frequencies
Play with color contrast
Right now we have to deal with the discrepancy of RGB/BGR values in images. We may want to consider
    converting to hex values before sending back to the frontend 
Create return value format (JSON structure) for the frontend 
Last step: convert to a format that allows processing to be executed with an http request!

Stretch goal: storage (might also be a frontend thing)
"""

def centroid_histogram(clt):
    # grab the number of different clusters and create a histogram
    # based on the number of pixels assigned to each cluster
    numLabels = np.arange(0, len(np.unique(clt.labels_)) + 1)
    (hist, _) = np.histogram(clt.labels_, bins=numLabels)

    # normalize the histogram, such that it sums to one
    hist = hist.astype("float")
    hist /= hist.sum()

    # return the histogram
    return hist


if __name__ == '__main__':
    img = cv2.imread('photos/ghost.jpg')
    img_copy = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Since the K-means algorithm we're about to do,
    # is very labour intensive, we will do it on a smaller image copy
    # This will not affect the quality of the algorithm
    pixelImage = img.reshape((img.shape[0] * img.shape[1], 3))
    # We use the sklearn K-Means algorithm to find the color histogram
    # from our small size image copy
    clt = KMeans(n_clusters=6)
    clt.fit(pixelImage)

    # build a histogram of clusters and then create a figure
    # representing the number of pixels labeled to each color
    hist = centroid_histogram(clt)
    print(hist)
    print(clt.cluster_centers_)