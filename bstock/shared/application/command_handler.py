from abc import ABC, abstractmethod
from typing import Generic, TypeVar

from bstock.shared.application.command import Command

T = TypeVar("T")

class CommandHandler(Generic[T], ABC):
    @abstractmethod
    def handle(self, query: Command) -> T:
        pass