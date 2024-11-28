import sys
import os

from lab2.interfaces.calculator_interface import Calculator

class AdvancedCalculator(Calculator):
    def __init__(self):
        super().__init__()

    def calculate(self, num1, num2, operator):
        if operator == '^':
            return num1 ** num2
        return super().calculate(num1, num2, operator)

    def get_operator(self):
        operator = super().get_operator()
        if operator not in ['+', '-', '*', '/', '√', '^']:
            print("Invalid operator! Please use +, -, *, /, √, or ^.")
            return self.get_operator()
        return operator


advanced_calculator = AdvancedCalculator()
advanced_calculator.run()