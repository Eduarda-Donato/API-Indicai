from models.usuario import Usuario

class UsuarioMemento:
    def __init__(self, estado: Usuario):
        self._estado = estado

    def get_estado(self) -> Usuario:
        return self._estado
