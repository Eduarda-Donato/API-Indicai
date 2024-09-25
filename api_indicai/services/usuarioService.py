from typing import List, Optional
from api_indicai.strategies.storageStrategy import StorageStrategy
from api_indicai.models.usuario import Usuario

class UsuarioService:
    def __init__(self, storage_strategy: StorageStrategy):
        self.storage_strategy = storage_strategy

    def create_usuario(self, usuario: Usuario) -> Usuario:
        
        self.storage_strategy.save(usuario)
        return usuario
    
    def get_usuarios(self) -> List[Usuario]:
        
        usuarios_db = self.storage_strategy.load_all()
        return [Usuario.model_validate(usuario_db) for usuario_db in usuarios_db]

    def get_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        
        usuario_db = self.storage_strategy.load(usuario_id)
        if usuario_db:
            return Usuario.model_validate(usuario_db)
        return None

    def update_usuario(self, usuario_id: int, usuario: Usuario) -> Optional[Usuario]:
        usuario_db = self.storage_strategy.update(usuario_id, usuario)
        if usuario_db:
            return Usuario.model_validate(usuario_db)
        return None

    def delete_usuario_id(self, usuario_id: int) -> bool:
        
        return self.storage_strategy.delete(usuario_id)
