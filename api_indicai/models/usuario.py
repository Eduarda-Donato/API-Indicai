from pydantic import BaseModel

class Usuario(BaseModel):
    id: int
    nome: str
    cpf: int
    telefone: str
