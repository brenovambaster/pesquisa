import cv2
import numpy as np


class ShowImages:
    def __init__(self, image_path):
        self.image_path = image_path

    def show(self, list_similar_imgs):
        """
         Display the 9 most similar images in a 3x3 grid.
        :param list_similar_imgs: [{''id': int, 'distance': float32, 'path_img': str},...]
        :return:
        """
        images = []
        # Loop over the paths of the 9 most similar images
        for i in list_similar_imgs[:9]:
            path = i['path_img'].replace("../", "")
            # Read the image
            image = cv2.imread(path)
            image = cv2.resize(image, (400, 300))
            distance_text = str(i['distance'])
            image = cv2.putText(
                image,  # Image object
                distance_text,  # Text to be added
                (32, 23),  # Position (x, y)
                cv2.FONT_HERSHEY_COMPLEX_SMALL,  # Font type
                1,  # Font scale (size)
                (255, 255, 0),  # Color (BGR)
                1,  # Thickness of the text
            )

            # Add a 3px padding to the image
            image = cv2.copyMakeBorder(image, 3, 3, 3, 3, cv2.BORDER_CONSTANT, value=[0, 0, 0])

            # Append the image to the list
            images.append(image)

        # Verificar se há exatamente 9 imagens
        if len(images) != 9:
            raise ValueError("O número de imagens deve ser exatamente 9 para formar uma grade 3x3.")

        # Definir o tamanho de cada imagem (incluindo a borda)
        img_height, img_width = images[0].shape[:2]

        # Criar uma imagem em branco para a grade 3x3
        grid_image = np.zeros((img_height * 3, img_width * 3, 3), dtype=np.uint8)

        # Colocar cada imagem na posição correta na grade
        for idx, image in enumerate(images):
            row = idx // 3
            col = idx % 3
            grid_image[row * img_height:(row + 1) * img_height, col * img_width:(col + 1) * img_width] = image

        # Exibir a imagem da grade
        cv2.imshow("Images", grid_image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
