from abc import ABC, abstractmethod

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

class Francais(Langue):
    def saluer(self, heure: int) -> str:
        if 6 <= heure < 18:
            return "Bonjour"
        else:
            return "Bonsoir"

    def feliciter(self) -> str:
        return "Bien dit !"

    def acquitter(self) -> str:
        return "Au revoir, passez une bonne journée !"

class Anglais(Langue):
    def saluer(self, heure: int) -> str:
        if 6 <= heure < 18:
            return "Good morning"
        else:
            return "Good evening"

    def feliciter(self) -> str:
        return "Well said!"

    def acquitter(self) -> str:
        return "Goodbye, have a nice day!"

class InterfaceAnalyseur(ABC):
    @abstractmethod
    def analyser_chaine(self, chaine: str) -> str:
        pass

class AnalyseurTexte(InterfaceAnalyseur):
    def __init__(self, langue: Langue):
        self.langue = langue

    def analyser_chaine(self, chaine: str) -> str:
        response = "Bonjour"

        mirrored_chaine = chaine[::-1]
        is_palindrome = chaine.lower().replace(" ", "") == mirrored_chaine.lower().replace(" ", "")

        response += mirrored_chaine
        if is_palindrome:
            response += " Bien dit"
        response += " Au Revoir"
        return response







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
