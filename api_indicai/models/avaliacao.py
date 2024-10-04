from pydantic import BaseModel, Field

class Avaliacao(BaseModel):
    id: int = Field(default=None)
    id_usuario: int = Field(default=None)
    id_prestador: int = Field(default=None)
    nota: int 
    descricao: str

    class Config:
        from_attributes = True