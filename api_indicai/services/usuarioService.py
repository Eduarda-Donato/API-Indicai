import logging
from typing import List, Optional
from api_indicai.strategies.storageStrategy import StorageStrategy
from api_indicai.models.usuario import Usuario

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class UsuarioService:
    def __init__(self, storage_strategy: StorageStrategy):
        self.storage_strategy = storage_strategy

    def create_usuario(self, usuario: Usuario) -> Optional[Usuario]:
        try:
            self.storage_strategy.save(usuario)
            logging.info("Usuário criado com sucesso.")
            return usuario
        except ValueError as ve:
            logging.error(f"Erro ao criar usuário: {ve}")
            return None
        except Exception as e:
            logging.exception("Erro inesperado ao criar usuário.")
            return None

    def get_usuarios(self) -> List[Usuario]:
        try:
            usuarios_db = self.storage_strategy.load_all()
            return [Usuario.from_attributes(usuario_db) for usuario_db in usuarios_db]
        except Exception as e:
            logging.exception("Erro inesperado ao obter usuários.")
            return []

    def get_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        try:
            usuario_db = self.storage_strategy.load(usuario_id)
            if usuario_db:
                return Usuario.from_attributes(usuario_db)
            logging.warning(f"Usuário com ID {usuario_id} não encontrado.")
            return None
        except Exception as e:
            logging.exception(f"Erro inesperado ao obter usuário por ID {usuario_id}.")
            return None

    def update_usuario(self, usuario_id: int, usuario: Usuario) -> Optional[Usuario]:
        try:
            usuario_db = self.storage_strategy.update(usuario_id, usuario)
            if usuario_db:
                logging.info(f"Usuário com ID {usuario_id} atualizado com sucesso.")
                return Usuario.from_attributes(usuario_db)
            logging.warning(f"Usuário com ID {usuario_id} não encontrado para atualização.")
            return None
        except Exception as e:
            logging.exception(f"Erro inesperado ao atualizar usuário com ID {usuario_id}.")
            return None

    def delete_usuario_id(self, usuario_id: int) -> bool:
        try:
            success = self.storage_strategy.delete(usuario_id)
            if success:
                logging.info(f"Usuário com ID {usuario_id} deletado com sucesso.")
            else:
                logging.warning(f"Usuário com ID {usuario_id} não encontrado para deleção.")
            return success
        except Exception as e:
            logging.exception(f"Erro inesperado ao deletar usuário com ID {usuario_id}.")
            return False
