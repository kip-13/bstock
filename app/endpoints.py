from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from bstock.shared.application.query_handler import QueryHandler
from bstock.application.get_stocks.dto import GetStocksDTO
from bstock.application.get_stocks.query import GetStocksQuery

from app.config.container import Container

router = APIRouter()

# Health router
@router.get('/ping')
def get_status():
    return {'data': 'pong'}

@router.get('/stocks')
@inject
def get_stocks(
        get_stocks_handler: QueryHandler[GetStocksDTO] = Depends(Provide[Container.get_stocks_handler]),
):
    query = GetStocksQuery()
    return get_stocks_handler.handle(query)
