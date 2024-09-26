from fastapi import APIRouter, Depends, HTTPException
from typing import List
from models.usuario import Usuario
from services.usuarioService import UsuarioService
from db.dependencies import get_usuario_service
from utils.validarUsuario import ValidarUsuario
from utils.criptografarSenha import CriptografarSenha

class UsuarioController:
    def __init__(self, usuario_service: UsuarioService = Depends(get_usuario_service)):
        self.router = APIRouter()
        self.usuario_service = usuario_service
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/", response_model=Usuario)
        def create_usuario(usuario: Usuario):
            # Valida o usuário antes de criar
            valido, erros = ValidarUsuario.validar(usuario)
            if not valido:
                raise HTTPException(status_code=400, detail=erros)

            # Criptografa a senha antes de salvar
            usuario.senha = CriptografarSenha.hash_senha(usuario.senha)
            return self.usuario_service.create_usuario(usuario)

        @self.router.get("/{usuario_id}", response_model=Usuario)
        def get_usuario(usuario_id: int):
            usuario = self.usuario_service.get_usuario_por_id(usuario_id)
            if usuario is None:
                raise HTTPException(status_code=404, detail="Usuário não encontrado")
            return usuario

        @self.router.get("/", response_model=List[Usuario])
        def read_usuarios():
            return self.usuario_service.get_usuarios()

        @self.router.put("/{usuario_id}", response_model=Usuario)
        def update_usuario(usuario_id: int, usuario: Usuario):
            # Valida o usuário antes de atualizar
            valido, erros = ValidarUsuario.validar(usuario)
            if not valido:
                raise HTTPException(status_code=400, detail=erros)

            updated_usuario = self.usuario_service.update_usuario(usuario_id, usuario)
            if updated_usuario is None:
                raise HTTPException(status_code=404, detail="Usuário não encontrado")
            return updated_usuario

        @self.router.delete("/{usuario_id}", response_model=dict)
        def delete_usuario(usuario_id: int):
            if self.usuario_service.delete_usuario_id(usuario_id):
                return {"status": "Usuário deletado com sucesso"}
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        @self.router.post("/login")
        def login(login: str, senha: str):
            usuario = self.usuario_service.get_usuario_por_login(login)
            if usuario is None or not CriptografarSenha.verificar_senha(senha, usuario.senha):
                raise HTTPException(status_code=401, detail="Login ou senha inválidos.")
            return {"message": "Login bem-sucedido!", "usuario": usuario}
