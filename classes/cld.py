import cv2
import numpy as np
from .interfaces.IExtractor import IExtractor


class CLD(IExtractor):
    """
    Color Layout Descriptor (CLD)
    """

    def __init__(self, num_blocks=8, num_bins=32):
        self.num_blocks = num_blocks
        self.num_bins = num_bins

    def extract_features(self, image):
        """
        Extracts the Color Layout Descriptor (CLD) features from an image.
        :param image:
        :return cld_vector:
        """

        # Converter a imagem para o espaço de cor HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        height, width, _ = hsv_image.shape

        cld_vector = []

        # Dividir a imagem em blocos
        block_height = height // self.num_blocks
        block_width = width // self.num_blocks

        for i in range(self.num_blocks):
            for j in range(self.num_blocks):
                # Obter o bloco atual
                block = hsv_image[i * block_height:(i + 1) * block_height,
                        j * block_width:(j + 1) * block_width]

                # Calcular o histograma de matiz do bloco
                hist = cv2.calcHist([block], [0], None, [self.num_bins], [0, 256])
                hist = cv2.normalize(hist, hist).flatten()

                # Adicionar o histograma ao vetor CLD
                cld_vector.extend(hist)

        return np.array(cld_vector)
