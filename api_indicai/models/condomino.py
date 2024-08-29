from .usuario import Usuario
from pydantic import Field
from sqlalchemy import Column, String

class Condomino(Usuario):
    login: str = Field(default=None)
    senha: str = Field(default=None)
    bloco: str = Field(default=None)
    ap: str = Field(default=None)
    
    login = Column(String, nullable=True)
    senha = Column(String, nullable=True)
    bloco = Column(String, nullable=True)
    ap = Column(String, nullable=True)

