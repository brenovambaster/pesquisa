from abc import ABC, abstractmethod

class  IExtractor(ABC):
    @abstractmethod
    def extract_features(self, image):
        pass
