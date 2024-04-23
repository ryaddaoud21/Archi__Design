from abc import ABC, abstractmethod

class Langue(ABC):
    @abstractmethod
    def saluer(self, heure: int) -> str:
        pass

    @abstractmethod
    def acquitter(self, heure: int) -> str:
        pass

    @abstractmethod
    def feliciter(self) -> str:
        pass
