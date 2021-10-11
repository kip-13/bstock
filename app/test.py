import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from bstock.application.get_stocks.query_handler import GetStocksQueryHandler
from bstock.application.get_stocks.query import GetStocksQuery


user = os.getenv("DB_USER", "root")
password = os.getenv("DB_PASSWORD", "123456")
server = os.getenv("DB_SERVER", "127.0.0.1:3312")
db_name = os.getenv("DB_NAME", "app")
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{user}:{password}@{server}/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

try:
    db = SessionLocal()
    handler = GetStocksQueryHandler(db)
    dto = handler.handle(GetStocksQuery(
        symbol='asd'
    ))
    print(dto)
finally:
    db.close()