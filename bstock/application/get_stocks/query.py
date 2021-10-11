from typing import Optional

from bstock.shared.application.query import Query

class GetStocksQuery(Query):
    symbol: Optional[str]
