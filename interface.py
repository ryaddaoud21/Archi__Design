from abc import ABC, abstractmethod

class InterfaceAnalyseur(ABC):
    @abstractmethod
    def analyser_chaine(self, chaine: str) -> str:
        pass

class AnalyseurTexte(InterfaceAnalyseur):
    def analyser_chaine(self, chaine: str) -> str:
        response = "Bonjour"

        mirrored_chaine = chaine[::-1]
        is_palindrome = chaine.lower().replace(" ", "") == mirrored_chaine.lower().replace(" ", "")

        response += mirrored_chaine
        if is_palindrome:
            response += " Bien dit"

        return response
