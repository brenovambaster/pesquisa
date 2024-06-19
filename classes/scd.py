import cv2
import numpy as np


class SCD:
    """
    Scalable Color Descriptor (SCD)
    """

    def __init__(self, num_blocks=8, num_bins=32):
        self.num_blocks = num_blocks
        self.num_bins = num_bins

    def extract_features(self, image):
        """
        Extracts the SCD features from an image.
        :param image:
        :return: features:  Vector of features
        """
        # Convert the image to the HSV color space
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        height, width, _ = hsv_image.shape

        features = []

        # Divide the image into blocks
        block_height = height // self.num_blocks
        block_width = width // self.num_blocks

        for i in range(self.num_blocks):
            for j in range(self.num_blocks):
                # Get the current block
                block = hsv_image[i * block_height:(i + 1) * block_height,
                        j * block_width:(j + 1) * block_width]

                # Calculate the color histogram for each channel (Hue, Saturation, Value)
                hist_hue = cv2.calcHist([block], [0], None, [self.num_bins], [0, 180])
                hist_saturation = cv2.calcHist([block], [1], None, [self.num_bins], [0, 256])
                hist_value = cv2.calcHist([block], [2], None, [self.num_bins], [0, 256])

                # Normalize the histograms
                hist_hue = cv2.normalize(hist_hue, hist_hue).flatten()
                hist_saturation = cv2.normalize(hist_saturation, hist_saturation).flatten()
                hist_value = cv2.normalize(hist_value, hist_value).flatten()

                # Concatenate the histograms to form the feature vector for the block
                block_features = np.concatenate((hist_hue, hist_saturation, hist_value))
                features.extend(block_features)

        return features
