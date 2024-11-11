logo = """
 _____________________
|  _________________  |
| | Pythonista      | |  .----------------.  .----------------.  .----------------.  .----------------.
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------'
|_____________________|
"""

print(logo)
first_number = int(input("What's the first number?: "))

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def compute(first_input):
    for symbol in operations:
        print(symbol)
        
    operation = input("Pick an operation: ")
    
    if operation not in operations:
        print("Please provide a valid operator")
        return compute(first_input)
    else:
        second_number = float(input("What's the next number?: "))    
        output = float(operations[operation](int(first_input), second_number))
    
    print(f"{float(first_input)} {operation} {second_number} = {output}")
    return go_again(output)

def go_again(input_value):
    repeat = input(f"Type 'y' to continue calculating with {float(input_value)}, or type 'n' to start a new calculation: ")

    if repeat.lower() == "y":
        compute(input_value)
    elif repeat.lower() == "n":
        print(logo)
        new_first_number = int(input("What's the first number?: "))
        compute(new_first_number)
    else:
        return

compute(first_number)
