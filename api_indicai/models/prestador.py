from .usuario import Usuario
from enums.servico import Servico


class Prestador(Usuario):
    tipoServico: Servico
