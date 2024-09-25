from fastapi import Depends, FastAPI
from api_indicai.controller.avaliacaoCotroller import AvaliacaoController
from api_indicai.controller.usuarioController import UsuarioController
from api_indicai.db.dependencies import get_usuario_service
from api_indicai.db.dependencies import get_db_session

def create_app() -> FastAPI:
    app = FastAPI()

    # Rota raiz
    @app.get("/")
    def read_root():
        return {"message": "Bem-vindo à API Indicai"}

    # Incluindo as rotas de usuário
    app.include_router(UsuarioController.router, dependencies=[Depends(get_usuario_service)])
    db_session = get_db_session()  # Obter a sessão do banco de dados
    avaliacao_controller = AvaliacaoController(db_session)
    app.include_router(avaliacao_controller.router, prefix="/api", tags=["avaliacoes"])

    return app

app = create_app()
