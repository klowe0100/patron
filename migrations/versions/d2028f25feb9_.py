"""empty message

Revision ID: d2028f25feb9
Revises: 981d0f4fdccf
Create Date: 2019-01-07 13:12:53.808847

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd2028f25feb9'
down_revision = '981d0f4fdccf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('square_client',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('application_id', sa.String(length=128), nullable=True),
    sa.Column('location_id', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('square_client')
    # ### end Alembic commands ###