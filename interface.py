from abc import ABC, abstractmethod
import datetime
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
        chaine_inverse = chaine[::-1]
        if chaine.lower() == chaine_inverse.lower():
            return f"{chaine} {self.langue.feliciter()}"
        else:
            return chaine_inverse


def main():
    langue = input("Choisissez votre langue (fr, en): ")
    if langue == 'fr':
        langue_instance = Francais()
    elif langue == 'en':
        langue_instance = Anglais()
    else:
        print("Langue non supportée")
        return

    analyser = AnalyseurTexte(langue_instance)

    heure = datetime.datetime.now().hour
    print(langue_instance.saluer(heure))

    while True:
        texte = input("Écrivez quelque chose: ")
        if texte.lower() == 'quit':
            print(langue_instance.acquitter())
            break

        print(analyser.analyser_chaine(texte))
        print(f"Mirroir: {texte[::-1]}")

if __name__ == "__main__":
    main()


