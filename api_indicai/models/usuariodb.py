from sqlalchemy import Column, Integer, String, Enum, Float
from api_indicai.enums.usuarios import Usuarios
from typing import Union
from api_indicai.db.singletonSession import Base
from models.condomino import Condomino
from models.prestador import Prestador

class UsuarioDB(Base):
    __tablename__ = 'usuarios'

    def __init__(self, usuario: Union[Condomino, Prestador]):
        self.id = usuario.id
        self.nome = usuario.nome
        self.tipousuario = usuario.tipousuario
        self.cpf = usuario.cpf
        self.telefone = usuario.telefone
        self.login = usuario.login
        self.senha = usuario.senha
        self.bloco = usuario.bloco
        self.ap = usuario.ap
        self.tiposervico = usuario.tiposervico
        self.notamedia = usuario.notamedia

    
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
    notamedia =  Column(Float, nullable=True) 


    __table_args__ = {'extend_existing': True}

