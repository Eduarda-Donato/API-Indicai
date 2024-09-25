from fastapi import APIRouter, HTTPException
from typing import List, Optional
from api_indicai.models.avaliacao import AvaliacaoDB  # Ajuste conforme necessário
from api_indicai.repositories.avaliacaoRepository import AvaliacaoRepository
from api_indicai.services.avaliacaoService import AvaliacaoService  # Ajuste conforme necessário
from api_indicai.db.session import Session  # Ajuste conforme necessário

class AvaliacaoController:
    router = APIRouter()
    
    def __init__(self, db_session: Session):
        self.avaliacao_service = AvaliacaoService(AvaliacaoRepository(db_session))

    @router.post("/avaliacoes/", response_model=AvaliacaoDB)
    def create_avaliacao(self, id_usuario: int, id_prestador: int, nota: int, descricao: Optional[str] = None):
        return self.avaliacao_service.create_avaliacao(id_usuario=id_usuario, id_prestador=id_prestador, nota=nota, descricao=descricao)
    
    @router.get("/avaliacoes/{id_usuario}/{id_prestador}", response_model=AvaliacaoDB)
    def get_avaliacao(self, id_usuario: int, id_prestador: int):
        avaliacao = self.avaliacao_service.get_avaliacao_por_id(id_usuario, id_prestador)
        if avaliacao is None:
            raise HTTPException(status_code=404, detail="Avaliação não encontrada")
        return avaliacao
    
    @router.get("/avaliacoes/", response_model=List[AvaliacaoDB])
    def read_avaliacoes(self):
        return self.avaliacao_service.get_avaliacoes()

    @router.put("/avaliacoes/{id_usuario}/{id_prestador}", response_model=AvaliacaoDB)
    def update_avaliacao(self, id_usuario: int, id_prestador: int, nota: Optional[int] = None, descricao: Optional[str] = None):
        updated_avaliacao = self.avaliacao_service.update_avaliacao(id_usuario, id_prestador, nota, descricao)
        if updated_avaliacao is None:
            raise HTTPException(status_code=404, detail="Avaliação não encontrada")
        return updated_avaliacao

    @router.delete("/avaliacoes/{id_usuario}/{id_prestador}", response_model=dict)
    def delete_avaliacao(self, id_usuario: int, id_prestador: int):
        if self.avaliacao_service.delete_avaliacao(id_usuario, id_prestador):
            return {"status": "Avaliação deletada com sucesso"}
        raise HTTPException(status_code=404, detail="Avaliação não encontrada")
