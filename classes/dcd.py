import cv2
import numpy as np

class DCD:
    def __init__(self, num_blocks=4):
        self.num_blocks = num_blocks

    def extract_features(self, image):
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

                # Calculate the dominant color for the block
                dominant_color = self.calculate_dominant_color(block)

                # Add the dominant color to the feature vector
                features.extend(dominant_color)

        return features

    def calculate_dominant_color(self, block):
        # Reshape the block to a 1D array
        reshaped_block = block.reshape(-1, block.shape[-1])

        # Calculate the histogram of the Hue channel
        hist_hue = cv2.calcHist([block], [0], None, [180], [0, 180])

        # Find the index of the bin with the maximum frequency
        max_bin_index = np.argmax(hist_hue)

        # Convert the bin index to the corresponding Hue value
        dominant_hue = max_bin_index

        # Calculate the mean value for the Saturation and Value channels
        mean_saturation = np.mean(reshaped_block[:, 1])
        mean_value = np.mean(reshaped_block[:, 2])

        return [dominant_hue, mean_saturation, mean_value]

    def calculate_distance(self, features1, features2):
        # Calculate the Euclidean distance between the feature vectors
        distance = np.linalg.norm(np.array(features1) - np.array(features2))
        return distance


# Example of usage
image1 = cv2.imread('images/buraco1.jpg')
image2 = cv2.imread('images/buraco2.jpg')

dcd = DCD()
features1 = dcd.extract_features(image1)
features2 = dcd.extract_features(image2)

print(f"Distance dcd: ",dcd.calculate_distance(features1, features2))