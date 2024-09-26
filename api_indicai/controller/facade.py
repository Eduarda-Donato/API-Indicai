from fastapi import APIRouter
from avaliacaoController import AvaliacaoController
from usuarioController import UsuarioController
from db.session import Session
from services.usuarioService import UsuarioService

class Facade:
    _instance = None

    def __new__(cls, db_session: Session):
        if cls._instance is None:
            cls._instance = super(Facade, cls).__new__(cls)
            cls._instance.router = APIRouter()
            cls._instance.avaliacao_controller = AvaliacaoController(db_session)
            cls._instance.usuario_controller = UsuarioController(UsuarioService(db_session))  # Injeção de dependência
            cls._instance.setup_routes()
        return cls._instance

    def setup_routes(self):
        # Registra as rotas do controller de avaliação
        self.router.include_router(self.avaliacao_controller.router, prefix="/avaliacoes", tags=["Avaliações"])
        
        # Registra as rotas do controller de usuário
        self.router.include_router(self.usuario_controller.router, prefix="/usuarios", tags=["Usuários"])