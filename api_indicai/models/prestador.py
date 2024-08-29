from .usuario import Usuario
from ..enums.servico import Servico
from pydantic import Field
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Enum, Integer

Base = declarative_base()

class Prestador(Usuario):
    tipoServico: Servico = Field(default=None)