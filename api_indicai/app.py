from fastapi import Depends, FastAPI
from api_indicai.controller.avaliacaoController import AvaliacaoController
from api_indicai.controller.usuarioController import UsuarioController
from api_indicai.controller.facade import Facade
from api_indicai.db.singletonSession import AppConfig

def create_app() -> FastAPI:
    app = FastAPI()
    app_config = AppConfig()

    # Rota raiz
    @app.get("/")
    def read_root():
        return {"message": "Bem-vindo à API Indicai"}

    # Incluindo as rotas de usuário
    db_session = app_config.get_db_session() 
    facade = Facade(db_session)
    app.include_router(facade.router)
    #app.include_router(UsuarioController.router, dependencies=[Depends(get_usuario_service)])
    ##db_session = AppConfig.get_db_session()  # Obter a sessão do banco de dados
    #avaliacao_controller = AvaliacaoController(db_session)
    #app.include_router(avaliacao_controller.router, prefix="/api", tags=["avaliacoes"])

    return app

app = create_app()
