import pyfiglet
from art import text2art
from colorama import Fore, Style

class Art:
    def __init__(self, user_input, font, color, width, height, custom_char):
        self.user_input = user_input
        self.font = font
        self.color = color
        self.width = int(width)
        self.height = int(height)
        self.custom_char = custom_char
        self.art = self.generate_art()

    def generate_art(self):
        return pyfiglet.figlet_format(self.user_input, font=self.font, width=self.width)
        return art.replace(' ', self.custom_char)

    def get_colored_art(self):
        return self.color + self.art + Style.RESET_ALL

    def save_to_file(self, filename):
        with open(filename, "w") as file:
            file.write(self.art)
        print(f"ASCII-art saved у '{filename}'")

    @staticmethod
    def preview_art(ascii_art):
        print("\nASCII art preview:\n")
        print(ascii_art)