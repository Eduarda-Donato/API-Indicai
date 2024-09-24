from fastapi import Depends, FastAPI
from api_indicai.controller.usuarioController import UsuarioController
from api_indicai.db.dependecies import get_usuario_service

def create_app() -> FastAPI:
    app = FastAPI()

    # Rota raiz
    @app.get("/")
    def read_root():
        return {"message": "Bem-vindo à API Indicai"}

    # Incluindo as rotas de usuário
    app.include_router(UsuarioController.router, dependencies=[Depends(get_usuario_service)])

    return app

app = create_app()