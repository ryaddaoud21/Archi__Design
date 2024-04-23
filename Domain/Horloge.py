from abc import ABC, abstractmethod


class Horloge(ABC):
    @abstractmethod
    def heure_actuelle(self) -> int:
        pass
