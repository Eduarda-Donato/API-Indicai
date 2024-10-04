from api_indicai.repositories.usuarioRepositoryInterface import UsuarioRepositoryInterface
from api_indicai.repositories.usuarioRepositoryInDB import UsuarioRepository
from api_indicai.repositories.usuarioRepositoryInMemory import UsuarioRepositoryInMemory
from typing import Optional

class UsuarioRepositoryFactory:
    @staticmethod
    def criar_repository(tipo: str, db_session = None) -> UsuarioRepositoryInterface:
        if tipo == "BD":
            if db_session is None:
                raise ValueError("db_session deve ser fornecido para o repositório do banco de dados.")
            return UsuarioRepository(db_session)
        elif tipo == "InMemory":
            return UsuarioRepositoryInMemory()
        else:
            raise ValueError(f"Tipo de repositório desconhecido: {tipo}")
