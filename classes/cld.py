import cv2
import numpy as np
from scipy.fftpack import dct


class CLD:
    def __init__(self, num_y_coeffs=6, num_cb_coeffs=3, num_cr_coeffs=3):
        """

        :param num_y_coeffs: Number of Y channel Discrete Cosine Transform coefficients to keep.
        :param num_cb_coeffs: Number of Cb channel Discrete Cosine Transform coefficients to keep.
        :param num_cr_coeffs: Number of Cr channel Discrete Cosine Transform coefficients to keep.
        """
        self.num_y_coeffs = num_y_coeffs
        self.num_cb_coeffs = num_cb_coeffs
        self.num_cr_coeffs = num_cr_coeffs

    def extract_features(self, image):
        """
        Extract the Color Layout Descriptor (CLD) features from an image.
        :param image: The image from which to extract the features.
        :return: A list of the extracted features.
        :rtype: numpy.array
        """
        # Convert the image from RGB to YCbCr
        ycbcr_image = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

        # Split the image into Y, Cb, and Cr channels
        y_channel, cb_channel, cr_channel = cv2.split(ycbcr_image)

        # Resize the channels to 8x8
        y_channel_resized = cv2.resize(y_channel, (8, 8))
        cb_channel_resized = cv2.resize(cb_channel, (8, 8))
        cr_channel_resized = cv2.resize(cr_channel, (8, 8))

        # Apply DCT to each channel
        y_dct = dct(dct(y_channel_resized.T, norm='ortho').T, norm='ortho')
        cb_dct = dct(dct(cb_channel_resized.T, norm='ortho').T, norm='ortho')
        cr_dct = dct(dct(cr_channel_resized.T, norm='ortho').T, norm='ortho')

        # Collect the DCT coefficients
        y_coeffs = self._collect_coeffs(y_dct, self.num_y_coeffs)
        cb_coeffs = self._collect_coeffs(cb_dct, self.num_cb_coeffs)
        cr_coeffs = self._collect_coeffs(cr_dct, self.num_cr_coeffs)

        # Normalize the coefficients
        y_coeffs = y_coeffs / np.linalg.norm(y_coeffs)
        cb_coeffs = cb_coeffs / np.linalg.norm(cb_coeffs)
        cr_coeffs = cr_coeffs / np.linalg.norm(cr_coeffs)

        # Combine the coefficients into a single feature vector
        feature_vector = np.concatenate([y_coeffs, cb_coeffs, cr_coeffs])

        return feature_vector.tolist()

    def _collect_coeffs(self, dct_block, num_coeffs):
        """
        This method collects the DCT coefficients from a given DCT block.
        It follows a zigzag order to collect the coefficients, which is a common practice in image processing tasks
        when working with DCT transformed blocks. The number of coefficients to collect is determined by the 'num_coeffs' parameter.

        :param dct_block: 2D array representing the DCT transformed block from which to collect the coefficients.
        :type dct_block: numpy.ndarray

        :param num_coeffs: The number of coefficients to collect from the DCT block.
        :type num_coeffs: int

        :return: A 1D array of the collected coefficients.
        :rtype: numpy.ndarray
        """
        zigzag_order = [
            (0, 0), (0, 1), (1, 0), (2, 0), (1, 1), (0, 2), (0, 3), (1, 2),
            (2, 1), (3, 0), (4, 0), (3, 1), (2, 2), (1, 3), (0, 4), (0, 5),
            (1, 4), (2, 3), (3, 2), (4, 1), (5, 0), (6, 0), (5, 1), (4, 2),
            (3, 3), (2, 4), (1, 5), (0, 6), (0, 7), (1, 6), (2, 5), (3, 4),
            (4, 3), (5, 2), (6, 1), (7, 0), (7, 1), (6, 2), (5, 3), (4, 4),
            (3, 5), (2, 6), (1, 7), (2, 7), (3, 6), (4, 5), (5, 4), (6, 3),
            (7, 2), (7, 3), (6, 4), (5, 5), (4, 6), (3, 7), (4, 7), (5, 6),
            (6, 5), (7, 4), (7, 5), (6, 6), (5, 7), (6, 7), (7, 6), (7, 7)
        ]
        coeffs = []
        for idx in range(num_coeffs):
            x, y = zigzag_order[idx]
            coeffs.append(dct_block[x, y])
        return np.array(coeffs)

    def compare(self, feat1, feat2):
        """
        Compute the distance between two feature vectors.
        :param feat1:
        :param feat2:
        :return: distance
        :rtype: float
        """
        distance = np.linalg.norm(np.array(feat1) - np.array(feat2))
        return distance
