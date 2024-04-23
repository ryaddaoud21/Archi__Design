from abc import ABC, abstractmethod

class Langue(ABC):
    @abstractmethod
    def saluer(self, heure: int) -> str:
        pass

    @abstractmethod
    def acquitter(self, heure: int) -> str:
        pass

    @abstractmethod
    def feliciter(self) -> str:
        pass

class Francais(Langue):
    def saluer(self, heure: int) -> str:
        if 6 <= heure < 12:
            return "Bonjour"
        elif 12 <= heure < 18:
            return "Bon après-midi"
        elif 18 <= heure < 22:
            return "Bonsoir"
        else:
            return "Bonne nuit"
    def acquitter(self, heure: int) -> str:
        if 6 <= heure < 12:
            return "Bonne journée"
        elif 12 <= heure < 18:
            return "Bonne après-midi"
        elif 18 <= heure < 22:
            return "Bonne soirée"
        else:
            return "Bonne nuit"

    def feliciter(self) -> str:
        return "Bien dit !"


class Anglais(Langue):
    def saluer(self, heure: int) -> str:
        if 6 <= heure < 12:
            return "Good Morning"
        elif 12 <= heure < 18:
            return "Good Afternoon"
        elif 18 <= heure < 22:
            return "Good Evening"
        else:
            return "Good Night"

    def acquitter(self, heure: int) -> str:
        return "Goodbye"

    def feliciter(self) -> str:
        return "Well said!"


class Horloge(ABC):
    @abstractmethod
    def heure_actuelle(self) -> int:
        pass


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
