"""stock_price_history_table

Revision ID: 05c182ac4aba
Revises: c91f54baf71d
Create Date: 2021-10-10 18:53:54.946531

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c182ac4aba'
down_revision = 'c91f54baf71d'
branch_labels = None
depends_on = None
table = "stock_price_history"

def upgrade():
    op.create_table(table, 
        sa.Column('id', sa.dialects.mysql.BIGINT, primary_key=True),
        sa.Column('stock_id', sa.dialects.mysql.BIGINT, sa.ForeignKey('stock.id'), nullable=False),
        sa.Column('created_at', sa.dialects.mysql.DATETIME, nullable=False),
        sa.Column('price', sa.dialects.mysql.DECIMAL(15, 4), nullable=False),
    )

    op.create_index('ik_stock_id_timeline', table, ['stock_id', 'created_at'])


def downgrade():
    op.drop_table(table)
