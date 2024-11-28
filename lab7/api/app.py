import sys
import os

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__))))

from service.user_service import UserService
from utils.history_manager import HistoryManager
from ui.console_interface import ConsoleInterface

class ApiApp():
    def run():
        uow = UserService()
        uow.load_users()

        history_manager = HistoryManager()

        interface = ConsoleInterface(uow, history_manager)

        while True:
            print(f"\n1. Customize font colors")
            print(f"2. Display users as table")
            print(f"3. Display users as list")
            print(f"4. Save data to file (JSON, CSV, TXT)")
            print(f"5. Validate email of a user by ID")
            print(f"6. Display query history")
            print(f"7. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                interface.set_colors()
            elif choice == "2":
                interface.display_users_table()
            elif choice == "3":
                interface.display_users_list()
            elif choice == "4":
                format = input("Enter file format (json, csv, txt): ").strip().lower()
                if format in ["json", "csv", "txt"]:
                    interface.save_data(format)
                else:
                    print("Invalid format. Try again.")
            elif choice == "5":
                interface.validate_user_email()
            elif choice == "6":
                history_manager.display_history()
            elif choice == "7":
                break
            else:
                print("Invalid choice. Try again.")

    if __name__ == "__main__":
        main()