from abc import ABC, abstractmethod

class SenhaInterface(ABC):
    @abstractmethod
    def gerar_senha(self) -> str:
        pass