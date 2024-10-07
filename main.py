class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, num: float) -> float:
        return self.number + num

    def sub(self, num: float) -> float:
        return self.number - num

    def div(self, num: float) -> float:
        return self.number / num

    def mul(self, num: float) -> float:
        return self.number * num

    def calculate(self, exp: str) -> float:
        symbols = {"+": self.add, "-": self.sub, "/": self.div, "*": self.mul}

        exp_list = exp.split()
        self.number = symbols[exp_list[0]](float(exp_list[1]))

obj_calc = Calculator("", 0.0)

while True:

    user_input = input(f"Įveskite išraišką(pvz.: + 5) {obj_calc.number} ")
    
    if user_input in "qQ":
        break

    obj_calc.calculate(user_input)
    print(f"Result: {obj_calc.number}")