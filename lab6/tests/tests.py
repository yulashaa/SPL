from io import StringIO
import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../..'))

import unittest
from lab2.classes.calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_addition(self):
        self.assertEqual(self.calc.calculate(-1, 4, '+'), 3)

    def test_subtraction(self):
        self.assertEqual(self.calc.calculate(5, -3, '-'), 8)
        self.assertEqual(self.calc.calculate(3, 5, '-'), -2)

    def test_multiplication(self):
        self.assertEqual(self.calc.calculate(0, 5, '*'), 0)
        self.assertEqual(self.calc.calculate(-3, 4, '*'), -12)

    def test_division(self):
        self.assertEqual(self.calc.calculate(10, 2, '/'), 5)
        self.assertEqual(self.calc.calculate(-10, 2, '/'), -5)
            
    def test_error_handling(self):
        with self.assertRaises(ValueError):
            self.calc.get_number('Enter a number: ')
        with self.assertRaises(ValueError):
            self.calc.calculate(-4, None, '√')
        with self.assertRaises(ZeroDivisionError):
            self.calc.calculate(10, 0, '/')
        