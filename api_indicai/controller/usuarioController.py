from typing import Union, List, Type
from models.condomino import Condomino
from models.prestador import Prestador
from enums.servico import Servico
from services.usuarioManager import UsuarioManager
from utils.validarUsuario import ValidarUsuario
from utils.criptografarSenha import CriptografarSenha

class UsuarioController:
    def __init__(self, manager: UsuarioManager):
        self.manager = manager

    def create_usuario(self, usuario: Union[Condomino, Prestador]) -> bool:
        valido, erros = ValidarUsuario.validar(usuario)
        if not valido:
            for erro in erros:
                print(erro)
            return False

        usuario.senha = CriptografarSenha.hash_senha(usuario.senha)
        self.manager.create_usuario(usuario)
        return True

    def get_usuario_por_id(self, id: int) -> Union[Condomino, Prestador, None]:
        return self.manager.get_usuario_por_id(id)

    def get_usuario_por_tipo(self, tipo: Type[Union[Condomino, Prestador]]) -> List[Union[Condomino, Prestador]]:
        return self.manager.get_usuario_por_tipo(tipo)

    def get_prestador_por_servico(self, servico: Servico) -> List[Prestador]:
        return self.manager.get_prestador_por_servico(servico)

    def update_usuario(self, id: int, usuario_atualizado: Union[Condomino, Prestador]) -> bool:
        valido, erros = ValidarUsuario.validar(usuario_atualizado)
        if not valido:
            for erro in erros:
                print (erro)
            return False
        
        if usuario_atualizado.senha:
            usuario_atualizado.senha = CriptografarSenha.hash_senha(usuario_atualizado.senha)  # Corrigido para usar hash_senha

        return self.manager.update_usuario(id, usuario_atualizado)
        
    def delete_usuario_por_id(self, id: int) -> bool:
        return self.manager.delete_usuario_id(id)
