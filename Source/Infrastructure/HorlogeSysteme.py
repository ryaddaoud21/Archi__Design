from Source.Domain.InterfaceHorloge import Horloge
import datetime


class HorlogeSysteme(Horloge):
    def heure_actuelle(self) -> int:
        return datetime.datetime.now().hour
