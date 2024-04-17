import cv2
import numpy as np


class CSD:

    def __init__(self):
        pass

    def color_structure_descriptor(self, image, num_blocks=8, num_bins=32):
        """
        Calculates the Color Structure Descriptor (CSD) for an image.

        Args:
            image (numpy.ndarray): The input image.
            num_blocks (int): The number of blocks to divide the image into.
            num_bins (int): The number of bins for the hue and saturation histograms.

        Returns:
            numpy.ndarray: The CSD vector representing the image.
        """
        # Converter a imagem para o espaço de cor HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        height, width, _ = hsv_image.shape

        csd_vector = []

        # Dividir a imagem em blocos
        block_height = height // num_blocks
        block_width = width // num_blocks

        for i in range(num_blocks):
            for j in range(num_blocks):
                # Obter o bloco atual
                block = hsv_image[i * block_height:(i + 1) * block_height,
                        j * block_width:(j + 1) * block_width]

                # Calcular o histograma de cores do bloco
                hist = cv2.calcHist([block], [0, 1], None, [num_bins, num_bins], [0, 180, 0, 256])
                hist = cv2.normalize(hist, hist).flatten()

                # Adicionar o histograma ao vetor CSD
                csd_vector.extend(hist)

        return np.array(csd_vector)

    def compare_images(self, image1, image2, num_blocks=8, num_bins=32):
        """
        Compares two images using the Color Structure Descriptor (CSD) algorithm.

        Args:
            image1_path (str): The file path of the first image.
            image2_path (str): The file path of the second image.
            num_blocks (int): The number of blocks to divide the image into.
            num_bins (int): The number of bins for the hue and saturation histograms.

        Returns:
            float: The distance between the two images based on the CSD algorithm.
                   Returns None if either image cannot be read.
        """

        # Se uma das imagens não puder ser lida, retornar None
        if image1 is None or image2 is None:
            return None

        # Extrair os descritores CSD
        csd1 = self.color_structure_descriptor(image1, num_blocks, num_bins)
        csd2 = self.color_structure_descriptor(image2, num_blocks, num_bins)

        # Calcular a distância CSD
        distance = self.csd_distance(csd1, csd2)

        return distance

    def csd_distance(self, csd1, csd2):
        """
        Calculates the Euclidean distance between two CSD (Color Structure Descriptor) vectors.

        Parameters:
        csd1 (numpy.ndarray): The first CSD vector.
        csd2 (numpy.ndarray): The second CSD vector.

        Returns:
        float: The Euclidean distance between csd1 and csd2.
        """
        return np.linalg.norm(np.array(csd1) - np.array(csd2))


# Exemplo de uso
csd = CSD()
image1_path = 'images/buraco1.jpg'
image2_path = 'images/buraco2.jpg'

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

distance = csd.compare_images(image1, image2, num_blocks=8, num_bins=32)
print("Distância entre as imagens (CSD):", distance)
