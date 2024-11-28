import json
import csv
from tabulate import tabulate
from colorama import Fore, init

from utils.email_validator import EmailValidator

def initialize_colorama():
    init(autoreset=True)
    
class ConsoleInterface:
    def __init__(self, uow, history_manager):
        self.uow = uow
        self.history_manager = history_manager
        self.font_color = None

    def set_colors(self):
        print("\nCustomize Colors:")
        user_color = input("Enter font color: ").strip().upper()

        if user_color:
            if user_color in dir(Fore):
                self.font_color = getattr(Fore, user_color)
                initialize_colorama()
            else:
                print("Invalid color input, defaulting to no color.")
                self.font_color = None
        else:
            print("No color applied, using default formatting.")
            self.font_color = None

    def display_users_table(self):
        headers = ["ID", "Name", "Username", "Email", "Website"]
        table = [
            [user['id'], user['name'], user['username'], user['email'], user['website']]
            for user in self.uow.get_users()
        ]
        
        if self.font_color:
            headers = [self.font_color + header for header in headers]

        result = tabulate(table, headers=headers, tablefmt="grid")
        print(result)
        self.history_manager.add_to_history("Display users as table", result)

    def display_users_list(self):
        result = ""
        for user in self.uow.get_users():
            result += f"ID: {user['id']}\n"
            result += f"Name: {user['name']}\n"
            result += f"Username: {user['username']}\n"
            result += f"Email: {user['email']}\n"
            result += f"Website: {user['website']}\n"
            result += "-" * 40 + "\n"
        
        print(result)
        self.history_manager.add_to_history("Display users as list", result)

    def validate_user_email(self):
        try:
            user_id = int(input("Enter the user ID to validate email: "))
            user = next(user for user in self.uow.get_users() if user['id'] == user_id)
            email = user['email']
            is_valid = EmailValidator.is_valid_email(email)
            if is_valid:
                result = f"Email '{email}' for user ID {user_id} is valid."
            else:
                result = f"Email '{email}' for user ID {user_id} is invalid."
            print(result)
            self.history_manager.add_to_history(f"Validate email for user ID {user_id}", result)
        except StopIteration:
            result = f"User with ID {user_id} not found."
            print(result)
            self.history_manager.add_to_history(f"Validate email for user ID {user_id}", result)
        except ValueError:
            result = "Invalid input. Please enter a numeric user ID."
            print(result)
            self.history_manager.add_to_history(f"Validate email for user ID {user_id}", result)

    def save_data(self, format):
        filename = f"users.{format}"
        users = self.uow.get_users()

        if format == "json":
            with open(filename, "w", encoding="utf-8") as file:
                json.dump(users, file, indent=4)
        elif format == "csv":
            with open(filename, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerow(["ID", "Name", "Username", "Email", "Website"])
                for user in users:
                    writer.writerow([user['id'], user['name'], user['username'], user['email'], user['website']])
        elif format == "txt":
            with open(filename, "w", encoding="utf-8") as file:
                for user in users:
                    file.write(f"ID: {user['id']}\n")
                    file.write(f"Name: {user['name']}\n")
                    file.write(f"Username: {user['username']}\n")
                    file.write(f"Email: {user['email']}\n")
                    file.write(f"Website: {user['website']}\n")
                    file.write("-" * 40 + "\n")

        result = f"Data saved to {filename}"
        print(result)
        self.history_manager.add_to_history(f"Save data to {filename}", result)