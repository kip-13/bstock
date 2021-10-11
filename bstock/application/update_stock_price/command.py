from bstock.shared.application.command import Command

class UpdateStockPriceCommand(Command):
    symbol: str
