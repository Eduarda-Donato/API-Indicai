import logging
from typing import List, Optional, Union
from ..strategies.storageStrategy import StorageStrategy
from ..models.usuario import Usuario


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class UsuarioService:
    def __init__(self, storage_strategy: StorageStrategy):
        self.storage_strategy = storage_strategy

    def create_usuario(self, usuario: Usuario) -> Usuario:
        self.storage_strategy.save(usuario)
        return usuario

    def get_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        return self.storage_strategy.load(usuario_id)

    def get_usuario_por_tipo(self, tipo: str) -> List[Usuario]:
        usuarios = self.storage_strategy.load_all()
        return [usuario for usuario in usuarios if usuario.tipoUsuario == tipo]

    def get_prestador_por_servico(self, tipo_servico: str) -> List[Usuario]:
        usuarios = self.storage_strategy.load_all()
        return [usuario for usuario in usuarios if usuario.tipoUsuario == 'prestador' and usuario.tipoServico == tipo_servico]

    def update_usuario(self, usuario_id: int, usuario: Usuario) -> Optional[Usuario]:
        return self.storage_strategy.update(usuario_id, usuario)

    def delete_usuario_id(self, usuario_id: int) -> bool:
        return self.storage_strategy.delete(usuario_id)