from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class AppConfig:
    def __init__(self, database_url: str):
        self.database_url = database_url
        self.engine = create_engine(self.database_url)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine)
        self.app = FastAPI()

    def get_db_session(self) -> Session:
        db_session = self.SessionLocal()
        try:
            yield db_session
        finally:
            db_session.close()

        
    def create_database(self):
        Base.metadata.create_all(bind=self.engine)