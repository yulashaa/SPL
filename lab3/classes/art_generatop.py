import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

import pyfiglet
from art import text2art
from colorama import Fore, Style
from classes.user_input import UserInput
from classes.art import Art

class ArtGenerator:
    def __init__(self):
        self.available_fonts = pyfiglet.FigletFont.getFonts()

    def run(self):
        user_input = UserInput.get_input("Enter a word or phrase to convert to ASCII art: ")
        font = UserInput.select_font(self.available_fonts)
        color = UserInput.select_color()
        
        width = UserInput.get_input("Enter the width for the ASCII art: ")
        height = UserInput.get_input("Enter the height for the ASCII art: ")

        custom_char = UserInput.get_input("Enter a character to use for ASCII art: ")

        ascii_art = Art(user_input, font, color, width, height, custom_char)
        colored_art = ascii_art.get_colored_art()

        Art.preview_art(colored_art)

        if UserInput.get_input("Do you want to save ASCII art? (y/n): ").lower() == 'y':
            ascii_art.save_to_file("ascii.txt")