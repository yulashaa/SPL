from abc import ABC, abstractmethod

class CalculatorInterface(ABC):

    @abstractmethod
    def get_number(self, prompt):
        pass

    @abstractmethod
    def get_operator(self):
        pass

    @abstractmethod
    def calculate(self, num1, num2, operator):
        pass

    @abstractmethod
    def store_in_memory(self, result):
        pass

    @abstractmethod
    def add_to_history(self, expression, result):
        pass

    @abstractmethod
    def view_history(self):
        pass

    @abstractmethod
    def run(self):
        pass
