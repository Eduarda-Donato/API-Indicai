from sqlalchemy import Column, Integer, String
from db.session import Base


class AvaliacaoDB(Base):
    __tablename__ = 'avaliacao'
    __table_args__ = {'schema': 'indicai'}

    id = Column(Integer, primary_key=True, index=True)
    id_usuario = Column(Integer, primary_key=True, index=True)
    id_prestador = Column(Integer, primary_key=True, index=True)
    nota = Column(Integer)
    descricao = Column(String,nullable=True)