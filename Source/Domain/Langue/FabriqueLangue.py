from Source.Domain import Langue
from Source.Domain.Langue.LanguesSupportees import Francais, Anglais


class FabriqueLangue:
    @staticmethod
    def creer_langue(langue: str) -> Langue:
        if langue == 'fr':
            return Francais()
        elif langue == 'en':
            return Anglais()
        # Ajoutez d'autres langues ici
        else:
            raise ValueError("Langue non supportée")
