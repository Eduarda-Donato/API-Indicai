from .usuario import Usuario
from pydantic import Field

class Condomino(Usuario):
    login: str = Field(default=None)
    senha: str = Field(default=None)
    bloco: str = Field(default=None)
    ap: str = Field(default=None)