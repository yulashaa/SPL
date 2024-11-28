import sys
import os

# додаємо до системного шляху директорію, яка містить модуль lab9 для коректного імпорту
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from lab9.task import RunnerFacade  # імпортуємо клас RunnerFacade з модуля lab9.task

def runner():
    runner_instance = RunnerFacade()  # створення екземпляра класу RunnerFacade
    while True:
        # виведення меню на екран
        print("\n Menu ")
        print("1) Run Program 1")
        print("2) Run Program 2")
        print("3) Run Program 3")
        print("4) Run Program 4")
        print("5) Run Program 5")
        print("6) Run Program 6")
        print("7) Run Program 7")
        print("8) Run Program 8")
        print("0) Exit")

        # отримання вибору користувача
        choice = input("Select a menu option: ")
        if choice == "0":
            print("Exiting!")  # повідомлення про вихід
            break  # завершення циклу та програми

        # виклик методу для запуску вибраної програми
        runner_instance.run_program(choice)

runner()  # виклик функції для запуску меню
