from abc import ABC, abstractmethod

# Interface base para todos os comandos
class CommandInterface(ABC):
    @abstractmethod
    def executar(self):
        pass
