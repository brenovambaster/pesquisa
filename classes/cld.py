import cv2
import numpy as np


class CLD:
    def __init__(self):
        pass

    def color_layout_descriptor(self, image, num_blocks=8, num_bins=32):
        """
        Calculates the Color Layout Descriptor (CLD) for the given image.

        Args:
            image (numpy.ndarray): The input image.
            num_blocks (int): The number of blocks to divide the image into.
            num_bins (int): The number of bins for the hue histogram.

        Returns:
            numpy.ndarray: The CLD vector representing the image.
        """
        # Converter a imagem para o espaço de cor HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        height, width, _ = hsv_image.shape

        cld_vector = []

        # Dividir a imagem em blocos
        block_height = height // num_blocks
        block_width = width // num_blocks

        for i in range(num_blocks):
            for j in range(num_blocks):
                # Obter o bloco atual
                block = hsv_image[i * block_height:(i + 1) * block_height,
                        j * block_width:(j + 1) * block_width]

                # Calcular o histograma de matiz do bloco
                hist = cv2.calcHist([block], [0], None, [num_bins], [0, 256])
                hist = cv2.normalize(hist, hist).flatten()

                # Adicionar o histograma ao vetor CLD
                cld_vector.extend(hist)

        return np.array(cld_vector)

    def cld_distance(self, cld1, cld2):
        """
        Calculates the CLD (Color Layout Descriptor) distance between two CLD vectors.

        Parameters:
        cld1 (array-like): The first CLD vector.
        cld2 (array-like): The second CLD vector.

        Returns:
        float: The CLD distance between the two CLD vectors.
        """
        return np.linalg.norm(np.array(cld1) - np.array(cld2))  # Euclidean distance
        # return cv2.compareHist(cld1, cld2, cv2.HISTCMP_CHISQR) # Chi-Squared distance

    def compare_images(self, image1, image2):
        """
        Compares two images using the CLD (Color Layout Descriptor) method.

        Args:
            image1_path (str): The file path of the first image.
            image2_path (str): The file path of the second image.

        Returns:
            float: The distance between the two images based on the CLD method.
                   Returns None if either of the images cannot be read.
        """

        # Se uma das imagens não puder ser lida, retornar None
        if image1 is None or image2 is None:
            return None

        NUM_BLOCKS = 8
        # Extrair os descritores CLD
        cld1 = self.color_layout_descriptor(image1, NUM_BLOCKS)
        cld2 = self.color_layout_descriptor(image2, NUM_BLOCKS)

        # Calcular a distância CLD
        distance = self.cld_distance(cld1, cld2)

        if distance is None:
            print("Erro ao comparar as imagens.")
        else:
            print(f"Distância CLD: {distance}")

        return distance


# ---------------- Exemplo de uso ----------------
# Exemplo de uso
image1 = cv2.imread('images/buraco1.jpg')
image2 = cv2.imread('images/buraco2.jpg')

cld = CLD()
distance = cld.compare_images(image1, image2)
