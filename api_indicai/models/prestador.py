from .usuario import Usuario
from ..enums.servico import Servico
from pydantic import Field
from sqlalchemy import Column, String


class Prestador(Usuario):
    tipoServico: Servico = Field(default=None)
    
    tipoServico = Column(String, nullable=True)
