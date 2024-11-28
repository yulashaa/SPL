import math

memory = 0
history = []

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError as e:
            print("Please enter a number.")
            raise e

def get_operator():
    while True:
        operator = input("Enter an operator (+, -, *, /, ^, √, %): ")
        if operator in ['+', '-', '*', '/', '^', '√', '%']:
            return operator
        print("Invalid operator! Please try again.")

def calculate(num1, num2, operator):
    try:
        if operator == '+':
            return num1 + num2
        elif operator == '-':
            return num1 - num2
        elif operator == '*':
            return num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not possible.")
            return num1 / num2
        elif operator == '^':
            return num1 ** num2
        elif operator == '√':
            if num1 < 0:
                raise ValueError("Square root of a negative number is not defined.")
            return math.sqrt(num1)
        elif operator == '%':
            return num1 % num2
    except (ZeroDivisionError, ValueError) as e:
        print(e)
        raise e

def store_in_memory(result):
    global memory
    memory = result
    print(f"Result {result} has been stored in memory.")

def add_to_history(expression, result):
    history.append(f"{expression} = {result}")

def view_history():
    if not history:
        print("History is empty.")
    else:
        print("Calculation history:")
        for record in history:
            print(record)

def main():
    while True:
        use_memory = input("Use value from memory? (yes/no): ").strip().lower() == "yes"
        if use_memory:
            num1 = memory
        else:
            num1 = get_number("Enter the first number: ")

        operator = get_operator()

        if operator == '√':
            result = calculate(num1, None, operator)
            expression = f"√{num1}"
        else:
            num2 = get_number("Enter the second number: ")
            result = calculate(num1, num2, operator)
            expression = f"{num1} {operator} {num2}"

        if result is not None:
            print(f"Result: {result}")
            add_to_history(expression, result)

            if input("Save the result in memory? (yes/no): ").strip().lower() == "yes":
                store_in_memory(result)

        if input("View calculation history? (yes/no): ").strip().lower() == "yes":
            view_history()

        if input("Do another calculation? (yes/no): ").strip().lower() != "yes":
            break