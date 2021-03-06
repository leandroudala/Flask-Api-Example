"""empty message

Revision ID: 52311a879f41
Revises: 3d4c1c0e8ce8
Create Date: 2020-03-27 23:55:35.260569

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '52311a879f41'
down_revision = '3d4c1c0e8ce8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projeto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('descricao', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projeto')
    # ### end Alembic commands ###
