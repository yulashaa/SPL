import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from functions.functions import main

class ConsoleCalculator:
    def run():
        main()