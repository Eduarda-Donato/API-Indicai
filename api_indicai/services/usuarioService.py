from typing import List, Optional
from api_indicai.repositories.usuarioRepositoryInDB import UsuarioRepository  # Ajuste o caminho conforme necessário
from api_indicai.repositories.usuarioRepositoryInterface import UsuarioRepositoryInterface
from models.usuario import Usuario
from utils.criptografarSenha import CriptografarSenha
from utils.validarUsuario import ValidarUsuario
from api_indicai.db.singletonSession import AppConfig

class UsuarioService:
    def __init__(self,usuario_repository: UsuarioRepositoryInterface):
        self.usuario_repository = usuario_repository

    def create_usuario(self, usuario: Usuario) -> Usuario:
        # Validação do usuário
        is_valid, erros = ValidarUsuario.validar(usuario)
        if not is_valid:
            raise ValueError(f"Erro(s) de validação: {', '.join(erros)}")

        # Criptografia da senha
        if usuario.tipousuario == "condomino":
            usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

        usuario_db = self.usuario_repository.adicifonar(usuario)
        return usuario_db

    def get_usuarios(self) -> List[Usuario]:
        usuarios_db = self.usuario_repository.listar_todos()
        return [Usuario.model_validate(usuario_db) for usuario_db in usuarios_db]

    def get_usuario_por_id(self, usuario_id: int) -> Optional[Usuario]:
        usuario_db = self.usuario_repository.buscar_por_id(usuario_id)
        if usuario_db:
            return Usuario.model_validate(usuario_db)
        return None

    def update_usuario(self, usuario_id: int, usuario: Usuario) -> Optional[Usuario]:
        # Validação do usuário
        is_valid, erros = ValidarUsuario.validar(usuario)
        if not is_valid:
            raise ValueError(f"Erro(s) de validação: {', '.join(erros)}")

        # Criptografa a senha se for fornecida
        if usuario.senha:
            usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

        usuario_db = self.usuario_repository.atualizar(usuario_id, usuario)
        if usuario_db:
            return Usuario.model_validate(usuario_db)
        return None

    def delete_usuario_id(self, usuario_id: int) -> bool:
        return self.usuario_repository.remover(usuario_id)
