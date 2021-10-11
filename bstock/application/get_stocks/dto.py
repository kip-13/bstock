from typing import List
from datetime import datetime
from pydantic import BaseModel

class GetStocksSharePriceDTO(BaseModel):
    interval: str
    lowest: float
    highest: float
    average: float

class GetStocksShareDTO(BaseModel):
    id: int
    symbol: str
    acquired_at: datetime
    total_acquired: int
    total_value: float
    statistics: GetStocksSharePriceDTO

class GetStocksDTO(BaseModel):
    data: List[GetStocksShareDTO]
