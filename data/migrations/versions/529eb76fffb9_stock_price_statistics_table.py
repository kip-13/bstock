"""stock_price_statistics_table

Revision ID: 529eb76fffb9
Revises: 05c182ac4aba
Create Date: 2021-10-10 19:03:05.273080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '529eb76fffb9'
down_revision = '05c182ac4aba'
branch_labels = None
depends_on = None
table = "stock_price_statistics"

def upgrade():
    op.create_table(table, 
        sa.Column('id', sa.dialects.mysql.BIGINT, primary_key=True),
        sa.Column('stock_id', sa.dialects.mysql.BIGINT, sa.ForeignKey('stock.id'), nullable=False),
        sa.Column('interval', sa.dialects.mysql.VARCHAR(100), nullable=False),
        sa.Column('created_at', sa.dialects.mysql.DATETIME, nullable=False),
        sa.Column('lowest_price', sa.dialects.mysql.DECIMAL(15, 4), nullable=False),
        sa.Column('highest_price', sa.dialects.mysql.DECIMAL(15, 4), nullable=False),
        sa.Column('average_price', sa.dialects.mysql.DECIMAL(15, 4), nullable=False),
    )

    op.create_index('ik_stock_statistics_1', table, ['stock_id', 'interval', 'created_at'])


def downgrade():
    op.drop_table(table)
