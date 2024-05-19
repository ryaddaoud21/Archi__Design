from Source.Domain.InterfaceLangue import Langue
from Source.Langue.MessagesLangue import MESSAGES_FR, MESSAGES_EN


class Francais(Langue):
    def saluer(self, heure: int) -> str:
        # Utilisation des messages de langue française
        return MESSAGES_FR['salutations']['matin'] if 6 <= heure < 12 else MESSAGES_FR['salutations']['soir']

    def acquitter(self, heure: int) -> str:
        # Utilisation des messages de langue française
        return MESSAGES_FR['acquittements']['journee'] if 6 <= heure < 12 else MESSAGES_FR['acquittements']['soiree']

    def feliciter(self) -> str:
        # Utilisation des messages de langue française
        return MESSAGES_FR['felicitation']


class Anglais(Langue):
    def saluer(self, heure: int) -> str:
        # Utilisation des messages de langue anglaise
        return MESSAGES_EN['salutations']['matin'] if 6 <= heure < 12 else MESSAGES_EN['salutations']['soir']

    def acquitter(self, heure: int) -> str:
        # Utilisation des messages de langue anglaise
        return MESSAGES_EN['acquittements']['journee'] if 6 <= heure < 12 else MESSAGES_EN['acquittements']['soiree']

    def feliciter(self) -> str:
        # Utilisation des messages de langue anglaise
        return MESSAGES_EN['felicitation']
