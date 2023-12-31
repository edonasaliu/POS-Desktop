"""empty message

Revision ID: 45956746a8d8
Revises: 3c6a3df010a3
Create Date: 2022-12-05 18:11:38.958513

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45956746a8d8'
down_revision = '3c6a3df010a3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('permissions', sa.Column('user_role', sa.Enum('staff', 'manager', 'owner', 'superadmin'), nullable=True))
    op.drop_column('permissions', 'user_type')
    op.add_column('user', sa.Column('user_role', sa.Enum('staff', 'manager', 'owner', 'superadmin'), nullable=True))
    op.drop_column('user', 'user_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_type', sa.VARCHAR(length=5), nullable=True))
    op.drop_column('user', 'user_role')
    op.add_column('permissions', sa.Column('user_type', sa.VARCHAR(length=10), nullable=True))
    op.drop_column('permissions', 'user_role')
    # ### end Alembic commands ###
