from .usuario import Usuario
from pydantic import Field
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Condomino(Usuario):
    login: str = Field(default=None)
    senha: str = Field(default=None)
    bloco: str = Field(default=None)
    ap: str = Field(default=None)