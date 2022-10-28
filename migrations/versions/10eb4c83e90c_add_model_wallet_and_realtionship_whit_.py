"""add model wallet and realtionship whit add  walletaccount

Revision ID: 10eb4c83e90c
Revises: 3883fabe2a50
Create Date: 2022-10-27 16:49:29.344383

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '10eb4c83e90c'
down_revision = '3883fabe2a50'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('wallet_account',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('cardholder', sa.String(length=255), nullable=True),
    sa.Column('type', sa.String(length=120), nullable=True),
    sa.Column('card_number', sa.Integer(), nullable=True),
    sa.Column('date_expiry', sa.Date(), nullable=True),
    sa.Column('cvv', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wallet',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.Column('wallet_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['wallet_id'], ['wallet_account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wallet')
    op.drop_table('wallet_account')
    # ### end Alembic commands ###