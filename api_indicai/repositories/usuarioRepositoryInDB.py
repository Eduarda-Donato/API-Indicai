from sqlalchemy.orm import Session
from typing import List, Optional
from api_indicai.repositories.usuarioRepositoryInterface import UsuarioRepositoryInterface
from models.usuariodb import UsuarioDB
from models.usuario import Usuario  
from fastapi import HTTPException

class UsuarioRepository(UsuarioRepositoryInterface):
    def __init__(self, db_session: Session):
        self.db_session = db_session

    def adicionar(self, usuario: UsuarioDB) -> Usuario:
        try:
            self.db_session.add(usuario)
            self.db_session.commit()
            self.db_session.refresh(usuario)  
            return Usuario.from_attributes(usuario)  
        except Exception as e:
            self.db_session.rollback()
            raise HTTPException(status_code=500, detail=str(e))

    def buscar_por_id(self, usuario_id: int) -> Optional[Usuario]:
        usuario = self.db_session.query(UsuarioDB).filter(UsuarioDB.id == usuario_id).first()
        return Usuario.from_attributes(usuario) if usuario else None  

    def listar_todos(self) -> List[Usuario]:
        usuarios_db = self.db_session.query(UsuarioDB).all()
        return [Usuario.from_attributes(usuario) for usuario in usuarios_db]  

    def remover(self, usuario_id: int) -> bool:
        usuario = self.buscar_por_id(usuario_id)
        if usuario:
            self.db_session.delete(usuario)
            self.db_session.commit()
            return True
        return False

    def atualizar(self, usuario_id: int, usuario_atualizado: UsuarioDB) -> Optional[Usuario]:
        usuario = self.buscar_por_id(usuario_id)
        if usuario:
            for key, value in usuario_atualizado.dict(exclude_unset=True).items():
                setattr(usuario, key, value)
            self.db_session.commit()
            return Usuario.from_attributes(usuario)  # Retorna a instância atualizada como Usuario Pydantic
        return None
