import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

from classes.art_generator import ArtRawGenerator

artgen = ArtRawGenerator()
artgen.run()