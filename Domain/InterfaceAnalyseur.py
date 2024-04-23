from abc import ABC, abstractmethod
from Domain.Langue import Langue
from Domain.Horloge import Horloge


class InterfaceAnalyseur(ABC):
    @abstractmethod
    def analyser_chaine(self, chaine: str) -> str:
        pass


class AnalyseurTexte(InterfaceAnalyseur):
    def __init__(self, langue: Langue, horloge: Horloge):
        self.langue = langue
        self.horloge = horloge


    def analyser_chaine(self, chaine: str) -> str:
        chaine_inverse = chaine[::-1]
        if chaine.lower() == chaine_inverse.lower():
            return f"{chaine}  {self.langue.feliciter()}"
        else:
            return chaine_inverse
