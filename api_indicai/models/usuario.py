from pydantic import BaseModel as PydanticBaseModel, Field
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel as PydanticBaseModel, Field
from ..enums.usuarios import Usuarios

Base = declarative_base()

class Usuario(Base, PydanticBaseModel):
    id: int = Field(default=None)
    nome: str
    tipoUsuario: Usuarios
    cpf: int
    telefone: str

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipoUsuario = Column(Enum(Usuarios))
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String)
    


