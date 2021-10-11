from abc import ABC, abstractmethod
from typing import Generic, TypeVar
from bstock.shared.application.query import Query
from sqlalchemy.orm import Session

T = TypeVar("T")

class QueryHandler(Generic[T], ABC):
    _db: Session

    def __init__(self, db: Session):
        self._db = db

    @abstractmethod
    def handle(self, query: Query) -> T:
        pass