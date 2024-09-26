from sqlalchemy.orm import Session
from typing import List, Optional
from models.usuario import Usuario, UsuarioDB 
from storageStrategy import StorageStrategy

class DBStorageStrategy(StorageStrategy):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def save(self, item: Usuario) -> None:
        usuario_db = UsuarioDB(item)
        self.db_session.add(usuario_db)
        self.db_session.commit()

    def load(self, item_id: int) -> Optional[UsuarioDB]:
        return self.db_session.query(UsuarioDB).filter(UsuarioDB.id == item_id).first()

    def load_all(self) -> List[UsuarioDB]:
        return self.db_session.query(UsuarioDB).all()

    def delete(self, item_id: int) -> bool:
        item = self.db_session.query(UsuarioDB).filter(UsuarioDB.id == item_id).first()
        if item:
            self.db_session.delete(item)
            self.db_session.commit()
            return True
        return False

    def update(self, item_id: int, item: UsuarioDB) -> Optional[UsuarioDB]:
        existing_item = self.db_session.query(UsuarioDB).filter(UsuarioDB.id == item_id).first()
        if existing_item:
            for key, value in item.__dict__.items():
                setattr(existing_item, key, value)
            self.db_session.commit()
            return existing_item
        return None
