from abc import ABC, abstractmethod

class UsuarioRepositoryInterface(ABC):
    @abstractmethod
    def adicionar(self, usuario):
        pass

    @abstractmethod
    def buscar_por_id(self, usuario_id: int):
        pass

    @abstractmethod
    def listar_todos(self):
        pass

    @abstractmethod
    def remover(self, usuario_id: int) -> bool:
        pass

    @abstractmethod
    def atualizar(self, usuario_id: int, usuario_atualizado):
        pass
