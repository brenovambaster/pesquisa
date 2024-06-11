import cv2
import numpy as np
from classes.descriptor import Descriptor
from classes.ImageReader import ImageReader
from classes.extract_info_file import FileProcessor
from classes.HTD2 import HTD

# Read the image
image1 = ImageReader("base_imgs_testes/229.jpg").read_image()

# Extract features from the image
htd_obj = Descriptor(image1, 'CLD')
feat_1 = htd_obj.extractor.extract_features(image1)

# Read the database file and recuperate the tuples
file_processor = FileProcessor('output/databaseCLD.txt')
data = file_processor.process_file()

# Transform the features of the image to a numpy array float32
h1 = np.array(feat_1, dtype=np.float32)

"""
NOTA: Ajuste provisório para que encontre as imagens próximas, essa busca deve ser de responsabilidade da classe 
`operador de busca`

Atencao: Em alguns casos, esse trecho não mostra a imagem mais próxima de fato, mas sim outras imagens que não 
são tão próximas. Isso se deve ao descritor utilizado
"""
distances = []
for i in data:
    h2 = np.array(i['features'], dtype=np.float32)
    distance_info = {
        'id': i['id'],
        'distance': float(htd_obj.extractor.compare(h1, h2)),
        'path_img': i['path']
    }
    distances.append(distance_info)

# Sort the distances and return the ids of the most similar images
distances = sorted(distances, key=lambda item: item['distance'])

# Print the 10 most similar images
print(distances[:10])
for i in distances[:10]:
    print(i['path_img'])

# Initialize an empty list to store the images
images = []

# Loop over the paths of the 9 most similar images
for i in distances[:9]:
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
        1  # Thickness of the text
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
