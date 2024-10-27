from services.usuarioService import UsuarioService
from commands.commandInvoker import CommandInvoker
from api_indicai.models.usuario import Usuario
from commands.usuarioCommands import (
    CriarUsuarioCommand,
    AtualizarUsuarioCommand,
    DeletarUsuarioCommand
)

class Facade:
    def __init__(self, db_session):
        self.usuario_service = UsuarioService(db_session)
        self.command_invoker = CommandInvoker()

    def criar_usuario(self, usuario: Usuario):
        command = CriarUsuarioCommand(self.usuario_service, usuario)
        return self.command_invoker.execute_command(command)

    def atualizar_usuario(self, usuario_id: int, usuario: Usuario):
        command = AtualizarUsuarioCommand(self.usuario_service, usuario_id, usuario)
        return self.command_invoker.execute_command(command)

    def deletar_usuario(self, usuario_id: int):
        command = DeletarUsuarioCommand(self.usuario_service, usuario_id)
        return self.command_invoker.execute_command(command)