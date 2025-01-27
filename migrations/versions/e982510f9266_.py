"""empty message

Revision ID: e982510f9266
Revises: 4c55e600a946
Create Date: 2020-06-05 14:07:17.712444

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e982510f9266'
down_revision = '4c55e600a946'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('todos', sa.Column('completed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###

    op.execute('UPDATE todos SET completed = False WHERE completed is NULL;')

    op.alter_column('todos', 'completed', nullable=False)


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('todos', 'completed')
    # ### end Alembic commands ###
