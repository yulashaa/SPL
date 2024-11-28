import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab1.runner.runner import ConsoleCalculator
from lab2.classes.calculator import Calculator
from lab3.classes.art_generatop import ArtGenerator
from lab4.classes.art_generator import ArtRawGenerator
from lab5.classes.shape import Shape
from lab6.tests.tests import TestCalculator
from lab7.api.app import ApiApp
from lab8.classes.data_loader import DataLoader

class RunnerFacade:
    def __init__(self):
        self.programs = {
            "1": ConsoleCalculator,
            "2": Calculator,
            "3": ArtGenerator,
            "4": ArtRawGenerator,
            "5": Shape,
            "6": TestCalculator,
            "7": ApiApp,
            "8": DataLoader,
        }

    def run_program(self, program_number):
        program = self.programs.get(program_number)
        if program:
            program.run()
        else:
            print("Incorrect choice. Try again.")