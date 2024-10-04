from fastapi import APIRouter, HTTPException
from typing import List, Optional
from api_indicai.models.avaliacaodb import AvaliacaoDB  
from api_indicai.models.avaliacao import Avaliacao
from api_indicai.repositories.avaliacaoRepository import AvaliacaoRepository
from api_indicai.services.avaliacaoService import AvaliacaoService  
from api_indicai.db.singletonSession import Session  

class AvaliacaoController:
    router = APIRouter()
    
    def __init__(self, db_session: Session):
        self.avaliacao_service = AvaliacaoService(AvaliacaoRepository(db_session))
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/", response_model=Avaliacao)
        def create_avaliacao(id_usuario: int, id_prestador: int, nota: int, descricao: Optional[str] = None):
            if nota < 0 or nota > 5:
                raise HTTPException(status_code=400, detail="Nota deve estar entre 0 e 5.")
                
            return self.avaliacao_service.create_avaliacao(id_usuario=id_usuario, id_prestador=id_prestador, nota=nota, descricao=descricao)

        @self.router.get("/{id_usuario}/{id_prestador}", response_model=Avaliacao)
        def get_avaliacao(id_usuario: int, id_prestador: int):
            avaliacao = self.avaliacao_service.get_avaliacao_por_id(id_usuario, id_prestador)
            if avaliacao is None:
                raise HTTPException(status_code=404, detail="Avaliação não encontrada")
            return avaliacao
        
        @self.router.get("/", response_model=List[Avaliacao])
        def read_avaliacoes():
            return self.avaliacao_service.get_avaliacoes()

        @self.router.put("/{id_usuario}/{id_prestador}", response_model=Avaliacao)
        def update_avaliacao(id_usuario: int, id_prestador: int, nota: Optional[int] = None, descricao: Optional[str] = None):
            # Validação da nota se fornecida
            if nota is not None and (nota < 0 or nota > 5):
                raise HTTPException(status_code=400, detail="Nota deve estar entre 0 e 5.")
                
            updated_avaliacao = self.avaliacao_service.update_avaliacao(id_usuario, id_prestador, nota, descricao)
            if updated_avaliacao is None:
                raise HTTPException(status_code=404, detail="Avaliação não encontrada")
            return updated_avaliacao

        @self.router.delete("/{id_usuario}/{id_prestador}", response_model=dict)
        def delete_avaliacao(id_usuario: int, id_prestador: int):
            if self.avaliacao_service.delete_avaliacao(id_usuario, id_prestador):
                return {"status": "Avaliação deletada com sucesso"}
            raise HTTPException(status_code=404, detail="Avaliação não encontrada")


