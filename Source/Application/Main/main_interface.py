from Source.Domain.Langue.FabriqueLangue import FabriqueLangue
from Source.Infrastructure.HorlogeSysteme import HorlogeSysteme
from Source.Domain.InterfaceAnalyseur import AnalyseurTexte


def choisir_langue():
    while True:
        langue_code = input("Choisissez votre langue (fr, en): ")
        try:
            langue = FabriqueLangue.creer_langue(langue_code)
            return langue
        except ValueError as e:
            print(f"Erreur: {e}")
            print("Langue non supportée. Veuillez choisir entre 'fr' pour le français et 'en' pour l'anglais.")


def afficher_salutation(langue, horloge):
    print(langue.saluer(horloge.heure_actuelle()))


def analyser_texte(analyseur, texte):
    resultat = analyseur.analyser_chaine(texte)
    print(resultat)
    print(f"Mirroir: {texte[::-1]}")


def main():
    langue = choisir_langue()
    horloge = HorlogeSysteme()
    analyser = AnalyseurTexte(langue, horloge)

    afficher_salutation(langue, horloge)

    while True:
        texte = input("Écrivez quelque chose: ")
        if texte.lower() == 'quit':
            print(langue.acquitter(horloge.heure_actuelle()))
            break

        analyser_texte(analyser, texte)


if __name__ == "__main__":
    main()
