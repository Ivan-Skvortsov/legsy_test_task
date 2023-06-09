"""added index to Product.nm_id

Revision ID: 79b99172beb3
Revises: e82557f888fb
Create Date: 2023-04-20 17:05:42.333966

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79b99172beb3'
down_revision = 'e82557f888fb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_products_nm_id'), 'products', ['nm_id'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_products_nm_id'), table_name='products')
    # ### end Alembic commands ###
