import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))

import lab1.functions.functions as cf # cf - calculator functions
from lab2.interfaces.calculator_interface import CalculatorInterface

class Calculator(CalculatorInterface):
    def __init__(self):
        self.__memory = 0
        self.__history = []

    def get_number(self, prompt):
        return cf.get_number(prompt)

    def get_operator(self):
        return cf.get_operator()

    def calculate(self, num1, num2, operator):
        return cf.calculate(num1, num2, operator)

    def store_in_memory(self, result):
        cf.store_in_memory(result)
        self.__memory = result

    def add_to_history(self, expression, result):
        cf.add_to_history(expression, result)

    def view_history(self):
        cf.view_history()

    def run(self):
        while True:
            use_memory = input("Use value from memory? (yes/no): ").strip().lower() == "yes"
            if use_memory:
                num1 = self.memory
            else:
                num1 = self.get_number("Enter the first number: ")

            operator = self.get_operator()

            if operator == '√':
                result = self.calculate(num1, None, operator)
                expression = f"√{num1}"
            else:
                num2 = self.get_number("Enter the second number: ")
                result = self.calculate(num1, num2, operator)
                expression = f"{num1} {operator} {num2}"

            if result is not None:
                print(f"Result: {result}")
                self.add_to_history(expression, result)

                if input("Save the result in memory? (yes/no): ").strip().lower() == "yes":
                    self.store_in_memory(result)

            if input("View calculation history? (yes/no): ").strip().lower() == "yes":
                self.view_history()

            if input("Do another calculation? (yes/no): ").strip().lower() != "yes":
                break