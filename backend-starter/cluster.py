import cv2
import numpy as np
from sklearn.cluster import KMeans


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