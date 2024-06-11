import classes.htd as htd
import cv2
import numpy as np

# Load the image
image1 = cv2.imread("images/buraco1.jpg")
image2 = cv2.imread("images/buraco2.jpg")

htd_distance = htd.HTD()


vector =htd_distance.extract_features(image1)

np.savetxt("output/test.txt",vector, delimiter=',', fmt='%f')