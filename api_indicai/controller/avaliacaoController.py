from fastapi import APIRouter, HTTPException
from typing import List, Optional
from models.avaliacao import AvaliacaoDB
from repositories.avaliacaoRepository import AvaliacaoRepository
from services.avaliacaoService import AvaliacaoService
from db.session import Session

class AvaliacaoController:
    def __init__(self, db_session: Session):
        self.router = APIRouter()
        self.avaliacao_service = AvaliacaoService(AvaliacaoRepository(db_session))
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/", response_model=AvaliacaoDB)
        def create_avaliacao(id_usuario: int, id_prestador: int, nota: int, descricao: Optional[str] = None):
            return self.avaliacao_service.create_avaliacao(id_usuario, id_prestador, nota, descricao)

        @self.router.get("/{id_usuario}/{id_prestador}", response_model=AvaliacaoDB)
        def get_avaliacao(id_usuario: int, id_prestador: int):
            avaliacao = self.avaliacao_service.get_avaliacao_por_id(id_usuario, id_prestador)
            if avaliacao is None:
                raise HTTPException(status_code=404, detail="Avaliação não encontrada")
            return avaliacao

        @self.router.get("/", response_model=List[AvaliacaoDB])
        def read_avaliacoes():
            return self.avaliacao_service.get_avaliacoes()

        @self.router.put("/{id_usuario}/{id_prestador}", response_model=AvaliacaoDB)
        def update_avaliacao(id_usuario: int, id_prestador: int, nota: Optional[int] = None, descricao: Optional[str] = None):
            updated_avaliacao = self.avaliacao_service.update_avaliacao(id_usuario, id_prestador, nota, descricao)
            if updated_avaliacao is None:
                raise HTTPException(status_code=404, detail="Avaliação não encontrada")
            return updated_avaliacao

        @self.router.delete("/{id_usuario}/{id_prestador}", response_model=dict)
        def delete_avaliacao(id_usuario: int, id_prestador: int):
            if self.avaliacao_service.delete_avaliacao(id_usuario, id_prestador):
                return {"status": "Avaliação deletada com sucesso"}
            raise HTTPException(status_code=404, detail="Avaliação não encontrada")
