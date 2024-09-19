from fastapi import APIRouter, Depends, HTTPException
from typing import List, Optional
from api_indicai.models.usuario import Usuario
from api_indicai.services.usuarioService import UsuarioService
from api_indicai.db.dependecies import get_usuario_service

class UsuarioController:
    router = APIRouter()

    @router.post("/usuarios/", response_model=Usuario)
    def create_usuario(usuario: Usuario, service: UsuarioService = Depends(get_usuario_service)):
        return service.create_usuario(usuario)
    
    @router.get("/usuarios/{usuario_id}", response_model=Usuario)
    def get_usuario(usuario_id: int, service: UsuarioService = Depends(get_usuario_service)):
        usuario = service.get_usuario_por_id(usuario_id)
        if usuario is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return usuario
    
    @router.get("/usuarios/", response_model=List[Usuario])
    def read_usuarios(
        tipo: Optional[str] = None,
        tipo_servico: Optional[str] = None,
        service: UsuarioService = Depends(get_usuario_service)
    ):
        #if tipo:
        #    return service.get_usuario_por_tipo(tipo)
        #if tipo_servico:
        #    return service.get_prestador_por_servico(tipo_servico)
        return service.get_usuarios()

    @router.put("/usuarios/{usuario_id}", response_model=Usuario)
    def update_usuario(usuario_id: int, usuario: Usuario, service: UsuarioService = Depends(get_usuario_service)):
        updated_usuario = service.update_usuario(usuario_id, usuario)
        if updated_usuario is None:
            raise HTTPException(status_code=404, detail="Usuário não encontrado")
        return updated_usuario

    @router.delete("/usuarios/{usuario_id}", response_model=dict)
    def delete_usuario(usuario_id: int, service: UsuarioService = Depends(get_usuario_service)):
        if service.delete_usuario_id(usuario_id):
            return {"status": "Usuário deletado com sucesso"}
        raise HTTPException(status_code=404, detail="Usuário não encontrado")
