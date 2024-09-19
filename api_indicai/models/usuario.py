from pydantic import BaseModel, Field
from sqlalchemy import Column, Integer, String, Enum
from api_indicai.enums.usuarios import Usuarios
from api_indicai.db.session import Base

class Usuario(BaseModel):
    id: int = Field(default=None)
    nome: str
    tipoUsuario: Usuarios
    cpf: str
    telefone: str

    class Config:
        from_attributes = True


class UsuarioDB(Base):
    __tablename__ = 'usuarios'
    __table_args__ = {'schema': 'indicai'}

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String)
    tipousuario = Column(Enum(Usuarios))
    cpf = Column(String, unique=True, index=True)
    telefone = Column(String)
    login = Column(String, nullable=True)
    senha = Column(String, nullable=True)
    bloco = Column(String, nullable=True)
    ap = Column(String, nullable=True)
    tiposervico = Column(String, nullable=True)  


