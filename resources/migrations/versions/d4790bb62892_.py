"""empty message

Revision ID: d4790bb62892
Revises: e8ad79f56336
Create Date: 2022-12-01 17:13:23.495015

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4790bb62892'
down_revision = 'e8ad79f56336'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_product', 'product', ['name', 'barcode', 'id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_product', table_name='product')
    # ### end Alembic commands ###
