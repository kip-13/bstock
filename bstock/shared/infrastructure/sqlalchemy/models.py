from dataclasses import dataclass
from dataclasses import field
from typing import List
from datetime import datetime
from sqlalchemy import Column, Table, MetaData, ForeignKey, desc
from sqlalchemy.dialects import mysql
from sqlalchemy.orm import registry
from sqlalchemy.orm import relationship

mapper_registry = registry()

@dataclass
class StockPriceStatistics:
    id: int = field(init=False)
    stock_id: int = field(init=False)
    interval: str
    created_at: datetime
    lowest_price: float = field(init=False)
    highest_price: float = field(init=False)
    average_price: float = field(init=False)

@dataclass
class Stock:
    id: int = field(init=False)
    symbol: str
    price: float
    statistics: List[StockPriceStatistics] = field(default_factory=list)

@dataclass
class StockHold:
    id: int = field(init=False)
    stock_id: int = field(init=False)
    created_at: datetime
    shares: int = field(init=False)
    profit_loss: float
    stock: Stock

@dataclass
class StockPriceHistory:
    id: int = field(init=False)
    stock_id: int = field(init=False)
    created_at: datetime
    price: float = field(init=False)

metadata_obj = MetaData()

stock = Table(
    'stock',
    metadata_obj,
    Column('id', mysql.BIGINT, primary_key=True),
    Column('symbol', mysql.VARCHAR(100), nullable=False),
    Column('price', mysql.DECIMAL(15,4), nullable=False),
)

stock_hold = Table(
    'stock_hold',
    metadata_obj,
    Column('id', mysql.BIGINT, primary_key=True),
    Column('stock_id', ForeignKey('stock.id'), nullable=False),
    Column('created_at', mysql.DATETIME, nullable=False),
    Column('shares', mysql.INTEGER, nullable=False),
    Column('profit_loss', mysql.DECIMAL(15, 4), nullable=False),
)

stock_price_history = Table(
    'stock_price_history',
    metadata_obj,
    Column('id', mysql.BIGINT, primary_key=True),
    Column('stock_id', mysql.BIGINT, ForeignKey('stock.id'), nullable=False),
    Column('created_at', mysql.DATETIME, nullable=False),
    Column('price', mysql.DECIMAL(15, 4), nullable=False),
)

stock_price_statistics = Table(
    'stock_price_statistics',
    metadata_obj,
    Column('id', mysql.BIGINT, primary_key=True),
    Column('stock_id', mysql.BIGINT, ForeignKey('stock.id'), nullable=False),
    Column('interval', mysql.VARCHAR(100), nullable=False),
    Column('created_at', mysql.DATETIME, nullable=False),
    Column('lowest_price', mysql.DECIMAL(15, 4), nullable=False),
    Column('highest_price', mysql.DECIMAL(15, 4), nullable=False),
    Column('average_price', mysql.DECIMAL(15, 4), nullable=False),
)

mapper_registry.map_imperatively(Stock, stock, properties={
    'statistics': relationship(StockPriceStatistics, backref='stock_price_statistics', lazy='joined')
})

mapper_registry.map_imperatively(StockHold, stock_hold, properties={
    'stock': relationship(Stock, backref='stock', lazy='joined')
})

mapper_registry.map_imperatively(StockPriceHistory, stock_price_history)

mapper_registry.map_imperatively(StockPriceStatistics, stock_price_statistics)
