import cv2
import numpy as np


class CSD:
    def __init__(self, num_bins=8):
        self.num_bins = num_bins

    def extract_features(self, image):
        """
        Extract the Color Structure Descriptor (CSD) features from an image.
        :param image: The image from which to extract the features.
        :return: A list of the extracted features.
        :rtype: numpy.array
        """
        # Convert the image to HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Calculate the histogram with the specified number of bins
        hist = cv2.calcHist([hsv_image], [0, 1, 2], None, [self.num_bins] * 3, [0, 256] * 3)

        # Normalize the histogram
        hist = cv2.normalize(hist, hist).flatten()

        return np.array(hist).tolist()

    def compare(self, feat1, feat2):
        """
        Compute the distance between two feature vectors using Euclidean distance.
        :param feat1: First feature vector.
        :param feat2: Second feature vector.
        :return: Distance between the feature vectors.
        :rtype: float
        """
        distance = np.linalg.norm(np.array(feat1) - np.array(feat2))
        return distance
