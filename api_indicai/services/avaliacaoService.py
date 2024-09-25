from typing import List, Optional
from api_indicai.models.avaliacao import AvaliacaoDB
from api_indicai.repositories.avaliacaoRepository import AvaliacaoRepository  # Ajuste o caminho conforme necessário

class AvaliacaoService:
    def __init__(self, avaliacao_repository: AvaliacaoRepository):
        self.avaliacao_repository = avaliacao_repository

    def create_avaliacao(self, id_usuario: int, id_prestador: int, nota: int, descricao: Optional[str] = None) -> AvaliacaoDB:
        """
        Cria uma nova avaliação.
        """
        return self.avaliacao_repository.adicionar(id_usuario, id_prestador, nota, descricao)

    def get_avaliacoes(self) -> List[AvaliacaoDB]:
        """
        Retorna todas as avaliações.
        """
        return self.avaliacao_repository.listar_todas()

    def get_avaliacao_por_id(self, id_usuario: int, id_prestador: int) -> Optional[AvaliacaoDB]:
        """
        Busca uma avaliação pelo ID do usuário e ID do prestador.
        """
        return self.avaliacao_repository.buscar_por_id(id_usuario, id_prestador)

    def update_avaliacao(self, id_usuario: int, id_prestador: int, nota: Optional[int] = None, descricao: Optional[str] = None) -> Optional[AvaliacaoDB]:
        """
        Atualiza uma avaliação existente.
        """
        return self.avaliacao_repository.atualizar(id_usuario, id_prestador, nota, descricao)

    def delete_avaliacao(self, id_usuario: int, id_prestador: int) -> bool:
        """
        Remove uma avaliação pelo ID do usuário e ID do prestador.
        """
        return self.avaliacao_repository.remover(id_usuario, id_prestador)
