from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import declarative_base
from api_indicai.enums.usuarios import Usuarios

Base = declarative_base()

class Usuario(BaseModel):
    id: int = Field(default=None)
    nome: str
    tipoUsuario: Usuarios
    cpf: int
    telefone: str

    class Config:
        from_attributes = True


class Usuario(Base):
    __tablename__ = 'usuarios'

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipoUsuario = Column(Enum(Usuarios))
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String)
    login = Column(String, nullable=True)
    senha = Column(String, nullable=True)
    bloco = Column(String, nullable=True)
    ap = Column(String, nullable=True)
    tipoServico = Column(String, nullable=True)  


