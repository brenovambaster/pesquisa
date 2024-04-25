import cv2
import numpy as np

class HTD:
    def __init__(self, num_blocks=4, num_bins=8):
        self.num_blocks = num_blocks
        self.num_bins = num_bins

    def extract_features(self, image):
        # Convertendo a imagem para o espaço de cores HSV
        hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

        # Normalizando o histograma para cada canal
        h, s, v = cv2.split(hsv_image)
        h_eq = cv2.equalizeHist(h)
        s_eq = cv2.equalizeHist(s)
        v_eq = cv2.equalizeHist(v)
        hsv_eq_image = cv2.merge([h_eq, s_eq, v_eq])

        # Dividindo a imagem normalizada em blocos
        height, width = hsv_eq_image.shape[:2]
        block_height = height // self.num_blocks
        block_width = width // self.num_blocks

        features = []

        for i in range(self.num_blocks):
            for j in range(self.num_blocks):
                # Obtendo o bloco atual
                block = hsv_eq_image[i*block_height:(i+1)*block_height, j*block_width:(j+1)*block_width]

                # Calculando o histograma de matiz do bloco
                hist_hue = cv2.calcHist([block], [0], None, [self.num_bins], [0, 180])
                hist_saturation = cv2.calcHist([block], [1], None, [self.num_bins], [0, 256])
                hist_value = cv2.calcHist([block], [2], None, [self.num_bins], [0, 256])

                # Normalizando os histogramas
                hist_hue = cv2.normalize(hist_hue, hist_hue).flatten()
                hist_saturation = cv2.normalize(hist_saturation, hist_saturation).flatten()
                hist_value = cv2.normalize(hist_value, hist_value).flatten()

                # Concatenando as características do bloco atual
                features.extend(hist_hue)
                features.extend(hist_saturation)
                features.extend(hist_value)

        return features

    def calculate_distance(self, features1, features2):
        # Calculando a distância euclidiana entre os vetores de características
        distance = np.linalg.norm(np.array(features1) - np.array(features2))
        return distance

def compare_images(image1, image2, num_blocks=4, num_bins=8):
    # Criando instância da classe HTD
    htd_extractor = HTD(num_blocks, num_bins)

    # Extraindo características de ambas as imagens
    features1 = htd_extractor.extract_features(image1)
    features2 = htd_extractor.extract_features(image2)

    # Calculando a distância normalizada entre as características extraídas
    distance = htd_extractor.calculate_distance(features1, features2)

    return distance

# Exemplo de uso
image1 = cv2.imread('images/buraco1.jpg')
image2 = cv2.imread('images/buraco2.jpg')

distance = compare_images(image1, image2, num_blocks=4, num_bins=8)
print("Distância entre as imagens:", distance)

# Escrever o vetor de características em um arquivo
htd = HTD()
features = htd.extract_features(image1)

caminho = '../output/features_HTD_1.txt'
np.savetxt(caminho, features, delimiter=',', fmt='%f')
