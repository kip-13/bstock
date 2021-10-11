"""stock_table

Revision ID: c91f54baf71d
Revises: 
Create Date: 2021-10-10 18:26:12.302947

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c91f54baf71d'
down_revision = None
branch_labels = None
depends_on = None
table = "stock"

def upgrade():
    op.create_table(table, 
        sa.Column("id", sa.dialects.mysql.BIGINT, primary_key=True),
        sa.Column("symbol", sa.dialects.mysql.VARCHAR(100), nullable=False),
        sa.Column("price", sa.dialects.mysql.DECIMAL(15,4), nullable=False),
    )

    op.create_index('ik_symbol', table, ["symbol"])

def downgrade():
    op.drop_table(table)
