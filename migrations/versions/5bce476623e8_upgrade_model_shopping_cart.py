"""Upgrade Model shopping_cart

Revision ID: 5bce476623e8
Revises: af2012ff520e
Create Date: 2022-10-28 17:37:32.888357

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5bce476623e8'
down_revision = 'af2012ff520e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('shopping_cart_article_id_fkey', 'shopping_cart', type_='foreignkey')
    op.drop_column('shopping_cart', 'article_id')
    op.drop_column('shopping_cart', 'quantity')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shopping_cart', sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=True))
    op.add_column('shopping_cart', sa.Column('article_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('shopping_cart_article_id_fkey', 'shopping_cart', 'game_articles', ['article_id'], ['id'])
    # ### end Alembic commands ###
