from .usuario import Usuario

class Condomino(Usuario):
    login: str
    senha: int
    bloco: str
    ap: str

