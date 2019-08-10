from calculator.model import CalculatorModel

class CalculatorController:
    def __init__(self, num1, num2):
        self.calc = CalculatorModel(num1, num2)

    def exec(self, op):
        if op == '+':
            result = self.calc.add()
        elif op == '-':
            result = self.calc.sub()
        elif op == '*':
            result = self.calc.mul()
        elif op == '/':
            result = self.calc.div()
        return result