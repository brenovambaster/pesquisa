import cv2
import numpy as np


class CSD:
    """
    Color Structure Descriptor (CSD)
    """
    def __init__(self, num_blocks=8, num_bins=32):
        self.num_blocks = num_blocks
        self.num_bins = num_bins
        pass

    def color_structure_descriptor(self, image):
        """
        Extracts the Color Structure Descriptor (CSD) features from an image.

        :param image: The image from which to extract the features.
        :return: The  CSD  features vector of the image.
        """

        # Converter a imagem para o espaço de cor HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        height, width, _ = hsv_image.shape

        csd_vector = []

        # Dividir a imagem em blocos
        block_height = height // self.num_blocks
        block_width = width // self.num_blocks

        for i in range(self.num_blocks):
            for j in range(self.num_blocks):
                # Obter o bloco atual
                block = hsv_image[i * block_height:(i + 1) * block_height,
                        j * block_width:(j + 1) * block_width]

                # Calcular o histograma de cores do bloco
                hist = cv2.calcHist([block], [0, 1], None, [self.num_bins, self.num_bins], [0, 180, 0, 256])
                hist = cv2.normalize(hist, hist).flatten()

                # Adicionar o histograma ao vetor CSD
                csd_vector.extend(hist)

        return np.array(csd_vector)

    def distance(self, csd1, csd2):
        """
        Calculates the CSD (Color Structure Descriptor) distance between two CSD vectors.
        :param csd1:
        :param csd2:
        :return:
        """
        return np.linalg.norm(np.array(csd1) - np.array(csd2))

    def run (self, image1, image2):
        """
        Run the CSD  algorithm on two images.
        :param image1:
        :param image2:
        """
        csd1 = self.color_structure_descriptor(image1)
        csd2 = self.color_structure_descriptor(image2)

        print("CSD Distance: ", self.distance(csd1, csd2))
        print("CSD Similarity: ", 1 / (1 + self.distance(csd1, csd2)))
        print("---------------------------------------")


