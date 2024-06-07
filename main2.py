import cv2
from classes import descriptor
from classes.extract_info_file import FileProcessor
# TODO: SE FOR A PRIMEIRA VEZ EM QUE RODA ESSE SCRIPT, DEVE COMPILAR O ARQUIVO scripts/generate_database.py ANTES DE EXECUTAR ESTE ARQUIVO

image1 = cv2.imread("images/6.jpg")
file_processor = FileProcessor('output/database.txt')
data = file_processor.process_file()

for i in data:
    descriptor_instance = descriptor.Descriptor(image1, "HTD", "euclidean", i['features'])
    print(f"Distance: {descriptor_instance.distance.calculated_distance} para id={i['id']}")
    #print(i['features'])