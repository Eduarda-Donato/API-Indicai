from typing import List, Optional
from strategies.storageStrategy import StorageStrategy
from models.usuario import Usuario
from utils.criptografarSenha import CriptografarSenha
from utils.validarUsuario import ValidarUsuario

class UsuarioService:
    def __init__(self, storage_strategy: StorageStrategy):
        self.storage_strategy = storage_strategy

    def create_usuario(self, usuario: Usuario) -> Usuario:
        # Validação do usuário
        is_valid, erros = ValidarUsuario.validar(usuario)
        if not is_valid:
            raise ValueError(f"Erro(s) de validação: {', '.join(erros)}")

        # Criptografia da senha
        usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

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
        is_valid, erros = ValidarUsuario.validar(usuario)
        if not is_valid:
            raise ValueError(f"Erro(s) de validação: {', '.join(erros)}")

        if usuario.senha:
            usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

        usuario_db = self.storage_strategy.update(usuario_id, usuario)
        if usuario_db:
            return Usuario.model_validate(usuario_db)
        return None

    def delete_usuario_id(self, usuario_id: int) -> bool:
        return self.storage_strategy.delete(usuario_id)