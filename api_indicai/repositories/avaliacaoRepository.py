from sqlalchemy.orm import Session
from typing import List, Optional
from ..models.avaliacao import AvaliacaoDB  # Ajuste o caminho conforme necessário


class AvaliacaoRepository:
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar(self, id_usuario: int, id_prestador: int, nota: int, descricao: Optional[str] = None) -> AvaliacaoDB:
        """
        Adiciona uma nova avaliação ao banco de dados.
        """
        nova_avaliacao = AvaliacaoDB(id_usuario=id_usuario, id_prestador=id_prestador, nota=nota, descricao=descricao)
        self.db_session.add(nova_avaliacao)
        self.db_session.commit()
        return nova_avaliacao

    def buscar_por_id(self, id_usuario: int, id_prestador: int) -> Optional[AvaliacaoDB]:
        """
        Busca uma avaliação pelo ID do usuário e ID do prestador.
        """
        return self.db_session.query(AvaliacaoDB).filter(
            AvaliacaoDB.id_usuario == id_usuario,
            AvaliacaoDB.id_prestador == id_prestador
        ).first()

    def listar_todas(self) -> List[AvaliacaoDB]:
        """
        Retorna todas as avaliações do banco de dados.
        """
        return self.db_session.query(AvaliacaoDB).all()

    def remover(self, id_usuario: int, id_prestador: int) -> bool:
        """
        Remove uma avaliação do banco de dados pelo ID do usuário e ID do prestador.
        """
        avaliacao = self.buscar_por_id(id_usuario, id_prestador)
        if avaliacao:
            self.db_session.delete(avaliacao)
            self.db_session.commit()
            return True
        return False

    def atualizar(self, id_usuario: int, id_prestador: int, nota: Optional[int] = None, descricao: Optional[str] = None) -> Optional[AvaliacaoDB]:
        """
        Atualiza uma avaliação existente no banco de dados.
        """
        avaliacao = self.buscar_por_id(id_usuario, id_prestador)
        if avaliacao:
            if nota is not None:
                avaliacao.nota = nota
            if descricao is not None:
                avaliacao.descricao = descricao
            self.db_session.commit()
            return avaliacao
        return None
