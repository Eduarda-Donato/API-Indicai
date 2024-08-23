import logging
from typing import List, Union, TypeVar, Type
from models.condomino import Condomino
from models.prestador import Prestador
from enums.servico import Servico

T = TypeVar('T', Condomino, Prestador)


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


class UsuarioManager:
    def __init__(self):
        self.usuarios: List[Union[Condomino,Prestador]] = []
        logging.info('UsuarioManager iniciado.')

    def create_usuario(self, usuario: Union[Condomino,Prestador]):
        self.usuarios.append(usuario)
        logging.info(f'Usuário criado: {usuario}')
        

    def get_usuario_por_tipo(self, tipo: Type[T]) -> List[T]:
        return [usuario for usuario in self.usuarios if isinstance(usuario,tipo)]
    
    def get_usuario_por_id(self, id: int) -> Union[Condomino, Prestador]:
        usuario = next((usuario for usuario in self.usuarios if usuario.id == id), None)
        if usuario is None:
            logging.warning(f'Usuário com id "{id}" não encontrado.')
        return usuario
    
    def get_prestador_por_servico(self, servico: Servico) -> List[Prestador]:
        prestadores = [usuario for usuario in self.usuarios if isinstance(usuario,Prestador) and usuario.tipoServico == servico]
        logging.info(f'Prestadores encontrados para o serviço {servico}: {prestadores}')
        return prestadores
        
    def update_usuario(self, id: int, usuario_atualizado: Union[Condomino,Prestador]) -> bool:
        usuario = self.get_usuario_por_id(id)
        if usuario:
            logging.info(f'Atualizando usuário: {usuario}')
            usuario.nome = usuario_atualizado.nome
            usuario.cpf = usuario_atualizado.cpf
            usuario.telefone = usuario_atualizado.telefone

            if isinstance(usuario, Condomino) and isinstance(usuario_atualizado, Condomino):
                usuario.login = usuario_atualizado.login
                usuario.senha = usuario_atualizado.senha
                usuario.bloco = usuario_atualizado.bloco
                usuario.ap = usuario_atualizado.ap
            elif isinstance(usuario, Prestador) and isinstance(usuario_atualizado, Prestador):
                usuario.tipoServico = usuario_atualizado.tipoServico

        logging.warning(f'Usuário com ID "{id}" não encontrado para atualização.')
        return False

    def delete_usuario_id(self, id: int) ->  bool:
        usuario = self.get_usuario_por_id(id)
        if usuario:
            self.usuarios.remove(usuario)
            logging.info(f'Usuário removido: {usuario}')
            return True
        logging.warning(f'Usuário com id "{id}" não encontrado para remoção.')
        return False 