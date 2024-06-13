# euclidiana, manhattan, minkowski ...

import numpy as np


class Distance:
    raio: int = 2

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2  # vetor de características de um elemento da base de dados a ser comparado
        self.calculated_distance = 0

    def set_p2(self, p2):
        self.p2 = p2

    def euclidean(self):
        return np.linalg.norm(np.array(self.p1) - np.array(self.p2))

    def manhattan(self):
        self.calculated_distance = np.abs(np.array(self.p1) - np.array(self.p2)).sum()
        return self.calculated_distance

    def minkowski(self):
        self.calculated_distance = np.power(np.power(np.abs(np.array(self.p1) - np.array(self.p2)), self.raio).sum(),
                                            1 / self.raio)
        return self.calculated_distance

    def calculate(self, distance_name, r=None):
        """
        
        :param distance_name: Nome da distância a ser calculada
        :param r: 
        :return: 
        """
        # implementer para minkowski receber 'r'
        if r is not None:
            self.raio = r

        distances = {
            "euclidean": self.euclidean,
            "manhattan": self.manhattan,
            "minkowski": self.minkowski
        }
        self.calculated_distance = distances[distance_name]()
        return self.calculated_distance
