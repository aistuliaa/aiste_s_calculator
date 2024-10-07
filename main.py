class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, sk: float) -> float:
        return self.number+sk


    def div(self) -> float:
        ...

    def mul(self) -> float:
        ...

    def calculate(self) -> float:
        ...