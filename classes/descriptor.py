# Recebe qual extrator de característica será utilizado ( CSD, CLD ou HTD) e a imagem. Retorna as features da imagem

from classes import cld, csd, dcd, scd,lbp
from classes import HTD2 as htd
from classes.distances import Distance
from classes.interfaces.IExtractor import IExtractor


class Descriptor:
    """
    The Descriptor class is responsible for managing the feature extraction process from an image.

    Attributes:
    extractor: An instance of a feature extractor class (HTD, CLD, CSD, DCD, SCD).
    distance: An instance of the Distance class.
    features: A numpy array containing the extracted features from the image.

    :return: array of features extracted from the image
    """

    def __init__(self, image, extractor_name):
        """
        :param image: (np.array): The image to be analyzed.
        :param extractor_name: (str): The name of the feature extractor to be used.
        """

        self.extractor = IExtractor
        self.distance = Distance
        self.set_extractor(extractor_name)
        self.features = self.extractor.extract_features(image)

    def set_extractor(self, extractor_string):
        """
        Define qual extrator de característica será utilizado ( CSD, CLD, HTD, DCD ou SCD)
        :param extractor_string: (str) Nome do extrator de característica a ser utilizado.
        :return:
        """
        extractors = {
            "HTD": htd.HTD,
            "CLD": cld.CLD,
            "CSD": csd.CSD,
            "DCD": dcd.DCD,
            "SCD": scd.SCD,
            "LBP": lbp.LBP,
        }

        if extractor_string in extractors:
            self.extractor = extractors[extractor_string]()
        else:
            raise ValueError("Invalid extractor")

    def compare(self, features2, distance_name):
        """

        :param distance_name: "euclidean", "manhattan", "minkowski
        :param features2: vetoor de características da imagem a ser comparada
        :return:
        """
        self.distance = Distance(self.features, features2)
        return self.distance.calculate(distance_name)
