"""empty message

Revision ID: 3d4c1c0e8ce8
Revises: 
Create Date: 2020-03-27 22:12:30.863856

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3d4c1c0e8ce8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tarefa',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('titulo', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.Column('data_expiracao', sa.Date(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tarefa')
    # ### end Alembic commands ###
