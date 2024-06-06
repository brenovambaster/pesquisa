# Recebe qual extrator de característica será utilizado ( CSD, CLD ou HTD) juntamente com qual distância
# e retorna o vetor de características da imagem.

from classes import htd, cld, csd, dcd, scd
from classes.distances import Distance
from classes.interfaces.IExtractor import IExtractor


class Descriptor:
    def __init__(self, image, extractor_name, distance_name,p2):
        self.extractor = IExtractor
        self.distance = Distance

        self.set_extractor(extractor_name)
        self.features = self.extractor.extract_features(image)
        self.calculate_distance(distance_name, self.features,p2)

    def set_extractor(self, extractor_string):
        # TODO: refatorar para usar um dicionário de extratores e instanciar o extrator correto

        extractors = {
            "HTD": htd.HTD,
            "CLD": cld.CLD,
            "CSD": csd.CSD,
            "DCD": dcd.DCD,
            "SCD": scd.SCD
        }

        if extractor_string in extractors:
            self.extractor = extractors[extractor_string]()
        else:
            raise ValueError("Invalid extractor")

    def calculate_distance(self, distance_string, features,p2):
        # p2 é o vetor de características de um elemento da base de dados a ser comparado

        self.distance = Distance(features,p2)
        return self.distance.calculate(distance_string)
