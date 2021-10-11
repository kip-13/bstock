"""stock_hold_table

Revision ID: 5a864c33bd49
Revises: 529eb76fffb9
Create Date: 2021-10-10 19:41:27.511136

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a864c33bd49'
down_revision = '529eb76fffb9'
branch_labels = None
depends_on = None
table = 'stock_hold'

def upgrade():
    op.create_table(table,
        sa.Column('id', sa.dialects.mysql.BIGINT, primary_key=True),
        sa.Column('stock_id', sa.dialects.mysql.BIGINT, sa.ForeignKey('stock.id'), nullable=False),
        sa.Column('created_at', sa.dialects.mysql.DATETIME, nullable=False),
        sa.Column('shares', sa.dialects.mysql.INTEGER, nullable=False),
        sa.Column('profit_loss', sa.dialects.mysql.DECIMAL(15, 4), nullable=False),
    )

def downgrade():
    pass
