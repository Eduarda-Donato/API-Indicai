from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from ..services.usuarioService import UsuarioService
from ..strategies.dbStorageStrategy import DBStorageStrategy

class AppConfig:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.app = FastAPI()
        self.setup_routes()

    def get_db_session(self) -> Session:
        db_session = self.SessionLocal()
        try:
            yield db_session
        finally:
            db_session.close()

    def get_usuario_service(self, db_session: Session) -> UsuarioService:
        db_storage = DBStorageStrategy(db_session)
        return UsuarioService(db_storage)

config = AppConfig("postgresql+psycopg2://user:password@localhost/dbname")


app = config.app