"""empty message

Revision ID: 3c6a3df010a3
Revises: 3d003389cf95
Create Date: 2022-12-02 10:45:56.896495

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3c6a3df010a3'
down_revision = '3d003389cf95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index('ix_product_barcode', 'product', [sa.text('barcode ASC')], unique=True)
    op.create_index('ix_product_id', 'product', [sa.text('id ASC')], unique=True)
    op.create_index('ix_product_name', 'product', [sa.text('name ASC')], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_product_name', table_name='product')
    op.drop_index('ix_product_id', table_name='product')
    op.drop_index('ix_product_barcode', table_name='product')
    # ### end Alembic commands ###
