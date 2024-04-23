from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Domain.Langue import Anglais, Francais
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme


def main():
    while True:
        langue = input("Choisissez votre langue (fr, en): ")
        if langue == 'fr':
            langue_instance = Francais()
            break
        elif langue == 'en':
            langue_instance = Anglais()
            break
        else:
            print("Langue non supportée. Veuillez choisir entre 'fr' pour le français et 'en' pour l'anglais.")

    horloge = HorlogeSysteme()
    analyser = AnalyseurTexte(langue_instance, horloge)

    print(langue_instance.saluer(horloge.heure_actuelle()))

    while True:
        texte = input("Écrivez quelque chose: ")
        if texte.lower() == 'quit':
            print(langue_instance.acquitter(horloge.heure_actuelle()))
            break

        print(analyser.analyser_chaine(texte))
        print(f"Mirroir: {texte[::-1]}")


if __name__ == "__main__":
    main()
