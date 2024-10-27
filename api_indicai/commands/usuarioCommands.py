from api_indicai.models.usuario import Usuario
from api_indicai.services.usuarioService import UsuarioService
from commands.commandInterface import CommandInterface


# Comando para criar um usuário
class CriarUsuarioCommand(CommandInterface):
    def __init__(self, usuario_service: UsuarioService, usuario: Usuario):
        self.usuario_service = usuario_service
        self.usuario = usuario

    def executar(self):
        return self.usuario_service.create_usuario(self.usuario)

# Comando para atualizar um usuário
class AtualizarUsuarioCommand(CommandInterface):
    def __init__(self, usuario_service: UsuarioService, usuario_id: int, usuario: Usuario):
        self.usuario_service = usuario_service
        self.usuario_id = usuario_id
        self.usuario = usuario

    def executar(self):
        return self.usuario_service.update_usuario(self.usuario_id, self.usuario)

# Comando para deletar um usuário
class DeletarUsuarioCommand(CommandInterface):
    def __init__(self, usuario_service: UsuarioService, usuario_id: int):
        self.usuario_service = usuario_service
        self.usuario_id = usuario_id

    def executar(self):
        return self.usuario_service.delete_usuario_id(self.usuario_id)
