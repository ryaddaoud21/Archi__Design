from abc import ABC, abstractmethod
from Source.Domain.InterfaceLangue import Langue
from Source.Domain.InterfaceHorloge import Horloge


class InterfaceAnalyseur(ABC):
    @abstractmethod
    def analyser_chaine(self, chaine: str) -> str:
        pass

class AnalyseurTexte:
    def __init__(self, langue: Langue, horloge: Horloge):
        self._langue = langue
        self._horloge = horloge

    def analyser_chaine(self, chaine: str) -> str:
        chaine_inverse = chaine[::-1]
        if self._est_palindrome(chaine):
            return f"{chaine}  {self._langue.feliciter()}"
        else:
            return chaine_inverse

    def _est_palindrome(self, chaine: str) -> bool:
        return chaine.lower() == chaine[::-1].lower()