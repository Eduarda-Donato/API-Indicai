"""Criar tabela usuarios

Revision ID: 9b3f794db709
Revises: 
Create Date: 2024-10-03 13:09:03.819148

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '9b3f794db709'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    # Comando para criar a tabela 'usuarios' no esquema 'indicai'
    op.create_table(
        'usuarios',
        sa.Column('id', sa.Integer, primary_key=True, index=True),
        sa.Column('nome', sa.String, nullable=False),
        sa.Column('tipousuario', sa.String),
        sa.Column('cpf', sa.String),
        sa.Column('telefone', sa.String),
        sa.Column('login', sa.String, unique=True, nullable=False),
        sa.Column('senha', sa.String, nullable=False),
        sa.Column('bloco', sa.String),
        sa.Column('ap', sa.String),
        sa.Column('tiposervico', sa.String),
        sa.Column('notamedia', sa.Numeric(3, 2)),
    )


def downgrade() -> None:
    # Comando para remover a tabela 'usuarios'
    op.drop_table('usuarios')
