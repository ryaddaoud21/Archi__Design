import datetime


def saluer(langue='fr'):
    heure = datetime.datetime.now().hour
    if langue == 'fr':
        if 6 <= heure < 18:
            return "Bonjour"
        else:
            return "Bonsoir"
    elif langue == 'en':
        if 6 <= heure < 18:
            return "Good morning"
        else:
            return "Good evening"
    else:
        return "Hello"


def est_palindrome(texte):
    texte_nettoye = ''.join(char.lower() for char in texte if char.isalnum())
    return texte_nettoye == texte_nettoye[::-1]


def dire_au_revoir(langue='fr'):
    heure = datetime.datetime.now().hour
    if langue == 'fr':
        if 6 <= heure < 18:
            return "Au revoir, passez une bonne journée !"
        else:
            return "Bonne nuit, à bientôt !"
    elif langue == 'en':
        if 6 <= heure < 18:
            return "Goodbye, have a nice day!"
        else:
            return "Good night, see you soon!"
    else:
        return "Goodbye!"


def main():
    langue = input("Choisissez votre langue (fr, en): ")
    print(saluer(langue))

    while True:
        texte = input("Écrivez quelque chose: ")
        if texte.lower() == 'quit':
            print(dire_au_revoir(langue))
            break

        if est_palindrome(texte):
            if langue == 'fr':
                print("Bien dit !")
            elif langue == 'en':
                print("Well said!")
            else:
                print("Well done!")
        print(f"Mirroir: {texte[::-1]}")


if __name__ == "__main__":
    main()
