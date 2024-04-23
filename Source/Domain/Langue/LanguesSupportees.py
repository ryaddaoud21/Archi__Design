from Source.Domain.InterfaceLangue import Langue


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