from colorama import Fore

class UserInput:
    @staticmethod
    def get_input(prompt):
        return input(prompt)

    @staticmethod
    def select_font(available_fonts):
        print("Available fonts:")
        for i, font in enumerate(available_fonts[:10]):
            print(f"{i + 1}. {font}")
        choice = int(UserInput.get_input("Choose a font number: ")) - 1
        return available_fonts[choice]

    @staticmethod
    def select_color():
        print("Available colors:")
        print("1. Red")
        print("2. Blue")
        print("3. Green")
        choice = int(UserInput.get_input("Choose fonr color number: "))
        if choice == 1:
            return Fore.RED
        elif choice == 2:
            return Fore.BLUE
        elif choice == 3:
            return Fore.GREEN
        else:
            return Fore.WHITE