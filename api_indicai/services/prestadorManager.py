import logging
from typing import List
from api_indicai.enums.servico import Servico
from api_indicai.models.prestador import Prestador

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class PrestadorManager:
    def __init__(self):
        self.prestadores: List[Prestador] = []
        logging.info('PrestadorManager iniciado.')

    def create_prestador(self, prestador:Prestador):
        self.prestadores.append(prestador)
        logging.info(f'Prestador criado: {prestador}')

    def read_prestadores(self) -> List[Prestador]:
        return self.prestadores
    
    def read_prestador_nome(self, nome: str) -> Prestador:
        for prestador in self.prestadores:
            if prestador.nome == nome:
                return prestador
        logging.warning(f'Prestador com nome "{nome}" não encontrado.')
        return None
    
    def read_prestador_servico(self, servico: Servico) -> List[Prestador]:
        escolhidos = List[Prestador] = []
        for prestador in self.prestadores:
            if prestador.tipoServico == servico:
                escolhidos.append(prestador)
        logging.info(f'Prestadores encontrados para o serviço {servico}: {escolhidos}')
        return escolhidos

    
    def update_prestador_nome(self, nome: str, prestador_atualizado: Prestador) -> bool:
        prestador = self.read_prestador_nome(nome)
        if prestador:
            logging.info(f'Atualizando prestador: {prestador}')
            prestador.nome = prestador_atualizado.nome
            prestador.cpf = prestador_atualizado.cpf
            prestador.telefone = prestador_atualizado.telefone
            prestador.endereco = prestador_atualizado.endereco
            prestador.tipoServico = prestador_atualizado.tipoServico
            logging.info(f'Prestador atualizado: {prestador}')
            return True
        logging.warning(f'Prestador com nome "{nome}" não encontrado para atualização.')
        return False
    
    def delete_prestador_nome(self, nome: str) -> bool:
        prestador = self.read_prestador_nome(nome)
        if prestador:
            self.prestadores.remove(prestador)
            logging.info(f'Prestador removido: {prestador}')
            return True
            logging.warning(f'Prestador com nome "{nome}" não encontrado para remoção.')
        return False
    
    
    
