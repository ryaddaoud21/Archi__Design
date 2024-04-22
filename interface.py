from abc import ABC, abstractmethod

class InterfaceAnalyseur(ABC):
    @abstractmethod
    def analyser_chaine(self, chaine: str) -> str:
        pass

class AnalyseurTexte(InterfaceAnalyseur):
    def analyser_chaine(self, chaine: str) -> str:
        response = "Bonjour"
        return response
