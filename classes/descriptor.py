# Recebe qual extrator de característica será utilizado ( CSD, CLD ou HTD) juntamente com qual distância
# e retorna o vetor de características da imagem.

from classes import htd, cld, csd, dcd, scd
from classes.distances import Distance
from classes.interfaces.IExtractor import IExtractor


class Descriptor:
    def __init__(self, image, extractor_name, distance_name):
        self.extractor = IExtractor
        self.distance = Distance

        self.set_extractor(extractor_name)
        self.features = self.extractor.extract_features(image)
        self.calculate_distance(distance_name, self.features)

    def set_extractor(self, extractor_string):
        # TODO: refatorar para usar um dicionário de extratores e instanciar o extrator correto

        if extractor_string == "HTD":
            self.extractor = htd.HTD()
        elif extractor_string == "CLD":
            self.extractor = cld.CLD()
        elif extractor_string == "CSD":
            self.extractor = csd.CSD()
        elif extractor_string == "DCD":
            self.extractor = dcd.DCD()
        elif extractor_string == "SCD":
            self.extractor = scd.SCD()
        else:
            raise ValueError("Invalid extractor")

    def calculate_distance(self, distance_string, features):
        # p2 é o vetor de características de um elemento da base de dados a ser comparado

        self.distance = Distance(features, p2=features)
        return self.distance.calculate(distance_string)
