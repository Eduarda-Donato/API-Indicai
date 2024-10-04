from api_indicai.models.usuario import Usuario
from api_indicai.enums.servico import Servico
from pydantic import Field

class Prestador(Usuario):
    tiposervico: Servico = Field(default=None)
    notamedia: float