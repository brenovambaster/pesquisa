import cv2
import numpy as np

from classes.descriptor import Descriptor
from classes.ImageReader import ImageReader
from classes.extract_info_file import FileProcessor
from classes.HTD2 import HTD

# Read the image
image1 = ImageReader("base_imgs_testes/8.jpg").read_image()

# Extract features from the image
htd_obj = Descriptor(image1, 'HTD')
feat_1 = htd_obj.extractor.extract_features(image1)

# Read the database file and recuperate the tuples
file_processor = FileProcessor('output/database.txt')
data = file_processor.process_file()

# Transform the features of the image to a numpy array float32
h1 = np.array(feat_1, dtype=np.float32)

"""
TODO: Compare the features of the image with the features of the all images in the database
NOTA:  Ajuste provisório para que encontre as imagens próximas, essa busca deve ser de responsabilidade da classe 
`operador de busca`

Atencao: Em alguns casos,  esse trecho não mostra a imagem mais próxima de fato, mas sim outras imagens que não 
são tão próximas 
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

# Print the 5 most similar images
print(distances[:5])


# Initialize an empty list to store the images
images = []

# Loop over the paths of the 5 most similar images
for i in distances[:5]:
    path = i['path_img'].replace("../", "")
    # Read the image
    image = cv2.imread(path)
    image = cv2.resize(image, (400, 300))

    # Add a 3px padding to the image
    image = cv2.copyMakeBorder(image, 3, 3, 3, 3, cv2.BORDER_CONSTANT, value=[0, 0, 0])

    # Append the image to the list
    images.append(image)

# Concatenate the images horizontally
concatenated_image = np.hstack(images)
# Display the concatenated image
cv2.imshow("Images", concatenated_image)
cv2.waitKey(0)

