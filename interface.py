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
        response += " Au Revoir"
        return response



class Langue(ABC):
    @abstractmethod
    def saluer(self, heure: int) -> str:
        pass

    @abstractmethod
    def feliciter(self) -> str:
        pass

    @abstractmethod
    def acquitter(self) -> str:
        pass



# Création d'une instance de la classe
analyseur = AnalyseurTexte()

# Exemples d'utilisation de la méthode analyser_chaine
texte1 = "bonjour"
resultat1 = analyseur.analyser_chaine(texte1)
print(resultat1)  # Bonjour ruojnob Au Revoir

texte2 = "kayak"
resultat2 = analyseur.analyser_chaine(texte2)
print(resultat2)  # Bonjour kayak Bien dit Au Revoir

texte3 = "Salut"
resultat3 = analyseur.analyser_chaine(texte3)
print(resultat3)  # Bonjour tulaS Au Revoir
