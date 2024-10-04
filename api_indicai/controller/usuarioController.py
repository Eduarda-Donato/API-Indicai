from fastapi import APIRouter, Depends, HTTPException
from typing import List, Union
from models.usuario import Usuario
from api_indicai.models.prestador import Prestador
from api_indicai.models.condomino import Condomino
from services.usuarioService import UsuarioService
from utils.validarUsuario import ValidarUsuario
from utils.criptografarSenha import CriptografarSenha

class UsuarioController:
    def __init__(self, usuario_service: UsuarioService):
        self.router = APIRouter()
        self.usuario_service = usuario_service
        self.setup_routes()

    def setup_routes(self):
        @self.router.post("/", response_model=Union[Condomino, Prestador])
        def create_usuario(usuario: Union[Condomino, Prestador]):
            # Valida o usuário antes de criar
            valido, erros = ValidarUsuario.validar(usuario)
            if not valido:
                raise HTTPException(status_code=400, detail=erros)

            # Criptografa a senha se o tipo de usuário for Condomino
            if usuario.tipousuario == "condomino":
                usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

            return self.usuario_service.create_usuario(usuario)

        @self.router.get("/{usuario_id}", response_model=Union[Condomino, Prestador])
        def get_usuario(usuario_id: int):
            usuario = self.usuario_service.get_usuario_por_id(usuario_id)
            if usuario is None:
                raise HTTPException(status_code=404, detail="Usuário não encontrado")
            return usuario

        @self.router.get("/", response_model=List[Union[Condomino, Prestador]])
        def read_usuarios():
            return self.usuario_service.get_usuarios()

        @self.router.put("/{usuario_id}", response_model=Union[Condomino, Prestador])
        def update_usuario(usuario_id: int, usuario: Usuario):
            # Valida o usuário antes de atualizar
            valido, erros = ValidarUsuario.validar(usuario)
            if not valido:
                raise HTTPException(status_code=400, detail=erros)

            # Criptografa a senha se o tipo de usuário for Condomino
            if usuario.tipousuario == "condomino" and usuario.senha:
                usuario.senha = CriptografarSenha.hash_senha(usuario.senha)

            updated_usuario = self.usuario_service.update_usuario(usuario_id, usuario)
            if updated_usuario is None:
                raise HTTPException(status_code=404, detail="Usuário não encontrado")
            return updated_usuario

        @self.router.delete("/{usuario_id}", response_model=dict)
        def delete_usuario(usuario_id: int):
            if self.usuario_service.delete_usuario_id(usuario_id):
                return {"status": "Usuário deletado com sucesso"}
            raise HTTPException(status_code=404, detail="Usuário não encontrado")

        @self.router.post("/login", response_model=dict)
        def login(login: str, senha: str):
            usuario = self.usuario_service.get_usuario_por_login(login)
            if usuario is None or not CriptografarSenha.verificar_senha(senha, usuario.senha):
                raise HTTPException(status_code=401, detail="Login ou senha inválidos.")
            return {"message": "Login bem-sucedido!", "usuario": usuario}
