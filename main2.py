import cv2
import numpy as np

from classes.descriptor import Descriptor
from classes.ImageReader import ImageReader
from classes.extract_info_file import FileProcessor
from classes.HTD2 import HTD

# Read the image
image1 = ImageReader("base_imgs_testes/67.jpg").read_image()

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
distances = {}
for i in data:
    h2 = np.array(i['features'], dtype=np.float32)
    distances[i['id']] = htd_obj.extractor.compare(h1, h2, cv2.HISTCMP_CORREL)


# list a 5 mais próximas
distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
distances = list(distances.items())[:5]

print(distances)

# Desejo salvar os caminhos das imagens em um vetor para que depois eu possa exibir as imagens uma ao lado da outra
#
for i in data:
    for id, distancia in distances:
        if i['id'] == id:
            path= i['path'].replace('.', '', 1)
            img= cv2.imread(path)
            img= cv2.resize(img, (500, 500))
            cv2.imshow('image',img)
            cv2.waitKey(0)
            break