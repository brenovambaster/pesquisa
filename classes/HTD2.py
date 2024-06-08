import cv2
import numpy as np

class HTD:
    """
    A class to compute and compare HSV histograms.

    Attributes
    ----------
    h_bins : int
        Number of bins for the hue channel histogram.
    s_bins : int
        Number of bins for the saturation channel histogram.
    v_bins : int
        Number of bins for the value channel histogram.
    """

    def __init__(self, h_bins=8, s_bins=8, v_bins=8):
        self.h_bins = h_bins
        self.s_bins = s_bins
        self.v_bins = v_bins

    def compute(self, image):
        """
        Compute the HSV histogram of an image.

        Parameters
        ----------
        image : array_like
            Input image.

        Returns
        -------
        list
            The HSV histogram.
        """
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        h_hist = cv2.calcHist([hsv_image], [0], None, [self.h_bins], [0, 180])
        s_hist = cv2.calcHist([hsv_image], [1], None, [self.s_bins], [0, 256])
        v_hist = cv2.calcHist([hsv_image], [2], None, [self.v_bins], [0, 256])

        h_hist = cv2.normalize(h_hist, h_hist).flatten()
        s_hist = cv2.normalize(s_hist, s_hist).flatten()
        v_hist = cv2.normalize(v_hist, v_hist).flatten()

        histogram = np.concatenate((h_hist, s_hist, v_hist))
        return np.array(histogram).tolist()

    def compare(self, hist1, hist2, method=cv2.HISTCMP_CORREL):
        """
        Compare two histograms.

        Parameters
        ----------
        hist1, hist2 : array_like
            Histograms to compare.
        method : int, optional
            Comparison method (default is cv2.HISTCMP_CORREL).

        Returns
        -------
        float
            The similarity between the histograms.
        """
        similarity = np.linalg.norm(np.array(hist1) - np.array(hist2))
        return similarity