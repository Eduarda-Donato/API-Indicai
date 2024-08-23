from typing import Union, List, Type
from models.condomino import Condomino
from models.prestador import Prestador
from enums.servico import Servico
from services.usuarioManager import UsuarioManager

class UsuarioController:
    def __init__(self, manager: UsuarioManager):
        self.manager = manager

    def create_usuario(self, usuario: Union[Condomino, Prestador]):
        self.manager.create_usuario(usuario)

    def get_usuario_por_id(self, id: int) -> Union[Condomino, Prestador, None]:
        return self.manager.get_usuario_por_id(id)

    def get_usuario_por_tipo(self, tipo: Type[Union[Condomino, Prestador]]) -> List[Union[Condomino, Prestador]]:
        return self.manager.get_usuario_por_tipo(tipo)

    def get_prestador_por_servico(self, servico: Servico) -> List[Prestador]:
        return self.manager.get_prestador_por_servico(servico)

    def update_usuario(self, id: int, usuario_atualizado: Union[Condomino, Prestador]) -> bool:
        return self.manager.update_usuario(id, usuario_atualizado)

    def delete_usuario_por_id(self, id: int) -> bool:
        return self.manager.delete_usuario_id(id)
