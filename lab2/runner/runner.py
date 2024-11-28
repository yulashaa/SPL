import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from classes.calculator import Calculator

calc = Calculator()
calc.run()