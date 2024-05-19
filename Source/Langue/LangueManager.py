from typing import Dict
from Source.Domain.InterfaceLangue import Langue
from Source.Langue.MessagesLangue import MESSAGES_FR,MESSAGES_EN
from Source.Langue.LanguesSupportees import Francais, Anglais

class LangueManager:
    langues_disponibles: Dict[str, Langue] = {
        'fr': Francais(),
        'en': Anglais()
    }

    @classmethod
    def ajouter_langue(cls, code_langue: str, langue: Langue):
        cls.langues_disponibles[code_langue] = langue

    @classmethod
    def creer_langue(cls, langue_code: str) -> Langue:
        if langue_code in cls.langues_disponibles:
            return cls.langues_disponibles[langue_code]
        else:
            raise ValueError("Langue non supportée")

    @classmethod
    def lister_langues_disponibles(cls):
        return list(cls.langues_disponibles.keys())
