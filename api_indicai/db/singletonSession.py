from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base


Base = declarative_base()

class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AppConfig, cls).__new__(cls)
            cls.database_url = "postgresql://avnadmin:AVNS_NGzNN3n0QEnjHmyp18m@indicai-pg-indicai.c.aivencloud.com:20466/defaultdb?sslmode=require"
            cls.engine = create_engine(cls.database_url)
            cls.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls.engine)
            cls.app = FastAPI()
        return cls._instance

    def get_db_session(self) -> Session:
        db_session = self.SessionLocal()
        try:
            return db_session
        except:
            db_session.rollback()
            raise
        finally:
            db_session.close()

    def create_database(self):
        Base.metadata.create_all(bind=self.engine)

