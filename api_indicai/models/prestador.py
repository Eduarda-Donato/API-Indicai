from .usuario import Usuario
from api_indicai.enums.servico import Servico


class Prestador(Usuario):
    endereco: str
    tipoServico: Servico
