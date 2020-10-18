import cv2
import pandas as pd
import numpy as np

from sklearn import svm

""" 
Training dataset defined as follows: 
Column 1: Classified Color 
Column 2: Blue value
Column 3: Green value
Column 4: Red value

0: white
1: black
2: pink
3: red
4: orange
5: yellow
6: green
7: blue
8: purple
9: grey
10: brown
"""

# load and display the image you want to use:
img = cv2.imread('inputs/rainbow.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)

# colors list contains the values we will replace classified colors with
# change to create a custom palette
colors = [
    # b   g  r
    [255, 255, 255],  # white, 0
    [1, 1, 1],  # black, 1
    [238, 130, 238],  # pink, 2
    [1, 1, 255],  # red, 3
    [1, 165, 255],  # orange, 4
    [1, 255, 255],  # yellow, 5
    [1, 200, 1],  # green, 6
    [255, 1, 1],  # blue, 7
    [130, 1, 100],  # purple, 8
    [128, 128, 128],  # grey, 9
    [49, 92, 137]  # brown, 10
]

# import the training dataset using a pandas library
color_train = pd.read_csv('data/set-twenties.csv')

color_train.head()

# split the training dataset into result & inputs
y_tr = color_train.iloc[:, 0]
X_tr = color_train.iloc[:, 1:]

# fit SVM function to the dataset, and make a model
SVM = svm.SVC(decision_function_shape="ovo").fit(X_tr, y_tr)
model2 = SVM.fit(X_tr, y_tr)

# load the image again - this will be your final product
last = cv2.imread('inputs/rainbow.jpg')

# for each pixel in the image, classify it to one of the colors
# (this takes a long time - like upwards of five minutes for a big image)
for row in range(len(img)):
    for col in range(len(img[row])):
        arr = np.array(img[row][col])
        pred = model2.predict(arr.reshape(1, -1))
        pred_val = pred[0]
        last[row][col] = colors[pred_val]

# show the result :)
cv2.imshow('result', last)
cv2.waitKey(0)
