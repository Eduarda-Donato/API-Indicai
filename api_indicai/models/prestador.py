from .condomino import Condomino
from enums.servico import Servico

class Prestador(Condomino):
    tipoServico: Servico
