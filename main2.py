import cv2
import numpy as np

from classes import descriptor
from classes.extract_info_file import FileProcessor
from classes.HTD2 import HTD

image1 = cv2.imread("base_imgs_testes/5.jpg")
file_processor = FileProcessor('output/database.txt')
htd_obj = HTD(8, 8, 8)
feat_1 = htd_obj.compute(image1)

data = file_processor.process_file()

h1 = np.array(feat_1, dtype=np.float32)
distances = {}
for i in data:
    h2 = np.array(i['features'], dtype=np.float32)
    distances[i['id']] = htd_obj.compare(h1, h2, cv2.HISTCMP_CORREL)


# list a 5 mais próximas
distances = {k: v for k, v in sorted(distances.items(), key=lambda item: item[1])}
distances = list(distances.items())[:5]

print(distances)


# cv2.imshow('image1', image1)
# for i in distances:
#     image = cv2.imread(i[0])
#     cv2.imshow(i[0], image)