import logging
from typing import List, Optional
from api_indicai.models.condomino import Condomino

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class CondominoManager:
    def __init__(self):
        self.condominos: List[Condomino] = []
        logging.info('CondominoManager iniciado.')

    def create_condomino(self, condomino: Condomino):
        self.condominos.append(condomino)
        logging.info(f'Condômino criado: {condomino}')

    def read_condominos(self) -> List[Condomino]:
        return self.condominos
    
    def read_condomino_nome(self, nome: str) -> Optional[Condomino]:
        for condomino in self.condominos:
            if condomino.nome == nome:
                return condomino
        logging.warning(f'Condômino com nome "{nome}" não encontrado.')
        return None
    
    def read_condomino_ap(self, bloco: str, ap: int) -> Optional[Condomino]:
        for condomino in self.condominos:
            if condomino.bloco == bloco and condomino.ap == ap:
                return condomino
        logging.warning(f'Condômino no bloco "{bloco}" e apartamento "{ap}" não encontrado.')
        return None

    def update_condomino_nome(self, nome: str, condomino_atualizado: Condomino) -> bool:
        condomino = self.read_condomino_nome(nome)
        if condomino:
            logging.info(f'Atualizando condômino: {condomino}')
            condomino.nome = condomino_atualizado.nome
            condomino.cpf = condomino_atualizado.cpf
            condomino.telefone = condomino_atualizado.telefone
            condomino.bloco = condomino_atualizado.bloco
            condomino.ap = condomino_atualizado.ap
            logging.info(f'Condômino atualizado: {condomino}')
            return True
        logging.warning(f'Condômino com nome "{nome}" não encontrado para atualização.')
        return False
    
    def delete_condomino_nome(self, nome: str) -> bool:
        condomino = self.read_condomino_nome(nome)
        if condomino:
            self.condominos.remove(condomino)
            logging.info(f'Condômino removido: {condomino}')
            return True
        logging.warning(f'Condômino com nome "{nome}" não encontrado para remoção.')
        return False
