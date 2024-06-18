import cv2
import numpy as np
from skimage.feature import local_binary_pattern


class LBP:
    def __init__(self, radius=1, n_points=8):
        self.radius = radius
        self.n_points = n_points

    def extract_features(self, image):
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        lbp = local_binary_pattern(gray_image, self.n_points, self.radius, method="uniform")
        (hist, _) = np.histogram(lbp.ravel(), bins=np.arange(0, self.n_points + 3),
                                 range=(0, self.n_points + 2))
        hist = hist.astype("float")
        hist /= (hist.sum() + 1e-6)  # Normalize the histogram
        return np.array(hist).tolist()

    def compare(self, feat1, feat2):
        distance = np.linalg.norm(feat1 - feat2)
        return distance
