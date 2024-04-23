from Source.Domain.InterfaceAnalyseur import AnalyseurTexte
from Source.Domain.Langue.FabriqueLangue import FabriqueLangue
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme


def main():
    while True:
        langue_code = input("Choisissez votre langue (fr, en): ")
        try:
            langue = FabriqueLangue.creer_langue(langue_code)
            break
        except ValueError as e:
            print(e)
            print("Langue non supportée. Veuillez choisir entre 'fr' pour le français et 'en' pour l'anglais.")


    horloge = HorlogeSysteme()
    analyser = AnalyseurTexte(langue, horloge)

    print(langue.saluer(horloge.heure_actuelle()))

    while True:
        texte = input("Écrivez quelque chose: ")
        if texte.lower() == 'quit':
            print(langue.acquitter(horloge.heure_actuelle()))
            break

        print(analyser.analyser_chaine(texte))
        print(f"Mirroir: {texte[::-1]}")


if __name__ == "__main__":
    main()
