"""empty message

Revision ID: df35545c106d
Revises: 341ca618494b
Create Date: 2020-06-05 16:03:06.716996

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df35545c106d'
down_revision = '341ca618494b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('todos', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    # ### end Alembic commands ###
