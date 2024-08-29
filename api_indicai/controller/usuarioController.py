from fastapi import APIRouter, HTTPException, Depends
from typing import List, Optional
from sqlalchemy.orm import Session
from api_indicai.models.usuario import Usuario
from api_indicai.services.usuarioService import UsuarioService
from api_indicai.strategies.dbStorageStrategy import DBStorageStrategy

router = APIRouter()

class UsuarioController:
    def __init__(self, service: UsuarioService):
        self.service = service

    @router.post("/usuarios/", response_model=Usuario)
    def create_usuario(self, usuario: Usuario):
        return self.service.create_usuario(usuario)
    
    @router.get("/usuarios/{usuario_id}", response_model=Usuario)
    def get_usuario(self, usuario_id: int):
        usuario = self.service.get_usuario_por_id(usuario_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario
    
    @router.get("/usuarios/")
    def read_usuarios(self, tipo: Optional[str] = None, tipo_servico: Optional[str] = None):
        if tipo:
            return self.service.get_usuario_por_tipo(tipo)
        if tipo_servico:
            return self.service.get_prestador_por_servico(tipo_servico)
        return self.service.storage_strategy.load_all()

    @router.put("/usuarios/{usuario_id}", response_model=Usuario)
    def update_usuario(self, usuario_id: int, usuario: Usuario):
        updated_usuario = self.service.update_usuario(usuario_id, usuario)
        if updated_usuario is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return updated_usuario

    @router.delete("/usuarios/{usuario_id}", response_model=dict)
    def delete_usuario(self, usuario_id: int):
        if self.service.delete_usuario_id(usuario_id):
            return {"status": "Usuário deletado com sucesso"}
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
