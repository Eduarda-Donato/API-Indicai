from .usuario import Usuario
from utils.criptografarSenha import CriptografarSenha

class Condomino(Usuario):
    login: str
    senha: str
    bloco: str
    ap: str

    def set_senha(self, senha: str):
        self.senha = CriptografarSenha.hash_senha(senha)

    def verificar_senha(self, senha: str) -> bool:
        return CriptografarSenha.verificar_senha(senha, self.senha)
