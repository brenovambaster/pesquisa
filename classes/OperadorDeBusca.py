import cv2
import numpy as np
from classes.descriptor import Descriptor
from classes.extract_info_file import FileProcessor

class SearchOperator:
    def __init__(self, data_file_path):
        self.data_file_path = data_file_path
        self.file_processor = FileProcessor(data_file_path)
        self.data = self.file_processor.process_file()

    def search_similar_images(self, input_image, extractor_name):
        # Extract features from the input image
        descriptor = Descriptor(input_image, extractor_name)
        input_features = np.array(descriptor.features, dtype=np.float32)

        # Compare the features of the input image with the features of all images in the database
        distances = {}
        for i in self.data:
            db_features = np.array(i['features'], dtype=np.float32)
            distances[i['id']] = descriptor.extractor.compare(input_features, db_features, cv2.HISTCMP_CORREL)

        # Sort the distances and return the ids of the most similar images
        sorted_distances = sorted(distances.items(), key=lambda item: item[1])
        similar_image_ids = [id for id, distance in sorted_distances[:5]]

        return sorted_distances


search_operator = SearchOperator('../output/database.txt')
image = cv2.imread('../base_imgs_testes/5.jpg')
similar_image_ids = search_operator.search_similar_images(image, 'HTD')
print(similar_image_ids)