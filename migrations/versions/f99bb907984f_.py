"""empty message

Revision ID: f99bb907984f
Revises: 2a17e1eb4aa9
Create Date: 2020-03-28 20:49:12.618754

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99bb907984f'
down_revision = '2a17e1eb4aa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('funcionario_projeto',
    sa.Column('projeto_id', sa.Integer(), nullable=False),
    sa.Column('funcionario_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['funcionario_id'], ['funcionario.id'], ),
    sa.ForeignKeyConstraint(['projeto_id'], ['projeto.id'], ),
    sa.PrimaryKeyConstraint('projeto_id', 'funcionario_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('funcionario_projeto')
    # ### end Alembic commands ###