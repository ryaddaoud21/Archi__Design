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

def main():
    langue = input("Choisissez votre langue (fr, en): ")
    print(saluer(langue))



if __name__ == "__main__":
    main()
