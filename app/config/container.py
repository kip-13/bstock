from dependency_injector import containers, providers

from bstock.shared.infrastructure.database import Database
from bstock.application.get_stocks.query_handler import GetStocksQueryHandler

class Container(containers.DeclarativeContainer):

    config = providers.Configuration()

    db = providers.Singleton(Database, user=config.db.user, password=config.db.password, server=config.db.server, db=config.db.name)

    get_stocks_handler = providers.Factory(
        GetStocksQueryHandler,
        db=db.provided.session,
    )

