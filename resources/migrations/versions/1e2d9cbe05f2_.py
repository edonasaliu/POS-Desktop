"""empty message

Revision ID: 1e2d9cbe05f2
Revises: 45956746a8d8
Create Date: 2022-12-11 23:24:56.244208

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1e2d9cbe05f2'
down_revision = '45956746a8d8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sale', sa.Column('is_regular', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sale', 'is_regular')
    # ### end Alembic commands ###
