import numpy as np
from classes.descriptor import Descriptor
from classes.extract_info_file import FileProcessor


class SearchOperator:
    EUCLIDEAN = 'euclidean'
    MANHATTAN = 'manhattan'

    def __init__(self, data_file_path):
        """
        :param data_file_path: (str) The path to the file containing the data.
        """
        self.data_file_path = data_file_path
        self.file_processor = FileProcessor(data_file_path)
        self.data = self.file_processor.process_file()

    def all_knn(self, input_image_search, extractor_name, k=5, distance_name=EUCLIDEAN):
        """
        Compute the k most similar images to the input image.

        :param distance_name: EUCLIDEAN, MANHATTAN
        :param k: The number of most similar images to return. Defaults to 5.
        :param extractor_name: (str) The name of the feature extractor to be used.
        :param input_image_search: (numpy.ndarray) The input image to compare with the images in the database.

        :return distances: [{'id': int, 'distance': float, 'path_img': str}]
        :rtype: list
        """
        # Extract features from the input image
        descriptor = Descriptor(input_image_search, extractor_name)
        input_features_search = np.array(descriptor.features, dtype=np.float32)


        # Read the database file and recuperate the tuples
        file_processor = FileProcessor(self.data_file_path)
        data = file_processor.process_file()
        distances = []
        for i in data:
            h2 = np.array(i['features'], dtype=np.float32)
            distance_info = {
                'id': i['id'],
                'distance': float(descriptor.compare(h2, distance_name)),
                'path_img': i['path']
            }
            distances.append(distance_info)

        # Sort the distances and return the ids of the most similar images
        distances = sorted(distances, key=lambda item: item['distance'])
        return distances[:k]
