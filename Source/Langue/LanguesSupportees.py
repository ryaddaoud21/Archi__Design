from Source.Domain.InterfaceLangue import Langue
from Source.Langue.MessagesLangue import MESSAGES_FR, MESSAGES_EN

class Francais(Langue):
    def saluer(self, heure: int) -> str:
        return f"{MESSAGES_FR['salutations']['matin']}" if 6 <= heure < 12 else f"{MESSAGES_FR['salutations']['soir']}"

    def acquitter(self, heure: int) -> str:
        return f"{MESSAGES_FR['acquittements']['journee']}" if 6 <= heure < 12 else f"{MESSAGES_FR['acquittements']['soiree']}"

    def feliciter(self) -> str:
        return MESSAGES_FR['felicitation']

class Anglais(Langue):
    def saluer(self, heure: int) -> str:
        return f"{MESSAGES_EN['salutations']['morning']}" if 6 <= heure < 12 else f"{MESSAGES_EN['salutations']['evening']}"

    def acquitter(self, heure: int) -> str:
        return f"{MESSAGES_EN['acquittements']['day']}" if 6 <= heure < 12 else f"{MESSAGES_EN['acquittements']['evening']}"

    def feliciter(self) -> str:
        return MESSAGES_EN['felicitation']
