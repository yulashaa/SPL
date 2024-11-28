import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from classes.user_input import UserInput
from classes.art_generatop import ArtGenerator
from classes.art import Art

artgen = ArtGenerator()
artgen.run()