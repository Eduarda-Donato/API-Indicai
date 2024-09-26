from pydantic import BaseModel, Field
from enums.usuarios import Usuarios
from db.session import Base

class Usuario(BaseModel):
    id: int = Field(default=None)
    nome: str
    tipousuario: Usuarios
    cpf: str
    telefone: str

    class Config:
        from_attributes = True


