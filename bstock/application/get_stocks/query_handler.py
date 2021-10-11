from typing import List
from datetime import datetime, timedelta

from bstock.application.get_stocks.dto import GetStocksDTO, GetStocksShareDTO, GetStocksSharePriceDTO
from bstock.application.get_stocks.query import GetStocksQuery
from bstock.shared.application.query_handler import QueryHandler
from bstock.shared.infrastructure.sqlalchemy import models

from sqlalchemy import desc, and_
from sqlalchemy.orm import joinedload, with_loader_criteria


class GetStocksQueryHandler(QueryHandler[GetStocksDTO]):
    def handle(self, query: GetStocksQuery) -> GetStocksDTO:
        with self._db() as conn:
            today = datetime.now().replace(hour=0,minute=0,second=0, microsecond=0)
            data: List[GetStocksShareDTO] = []
            holds: List[models.StockHold] = conn \
                .query(models.StockHold) \
                .options(
                    joinedload(models.StockHold.stock).joinedload(models.Stock.statistics),
                    with_loader_criteria(
                        models.StockPriceStatistics,
                        and_(models.StockPriceStatistics.interval == 'daily', models.StockPriceStatistics.created_at >= today)
                    )
                ).all()

            for hold in holds:
                last_statistic = hold.stock.statistics.pop()
                statistics = GetStocksSharePriceDTO(
                    interval=last_statistic.interval,
                    lowest=last_statistic.lowest_price,
                    highest=last_statistic.highest_price,
                    average=last_statistic.average_price,
                )
                item = GetStocksShareDTO(
                    id=hold.id,
                    symbol=hold.stock.symbol,
                    acquired_at=hold.created_at,
                    total_acquired=hold.shares,
                    total_value=hold.shares*hold.stock.price,
                    statistics=statistics,
                )

                data.append(item)
            
            return GetStocksDTO(
                data=data
            )