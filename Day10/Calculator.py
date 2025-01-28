# Отримати число перше
# Вибрати дію
# Отримати друге число
# Вивести результат

import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def get_number(which_number):
    invalid_input = True
    num = ''

    while invalid_input:

        num = input(f"What is the {which_number} number?: ")
        invalid_input = False

        for symbol in num:
            if symbol not in "1234567890":
                invalid_input = True

    return int(num)

def get_operation():
    invalid_input = True
    operation = ""

    while invalid_input:

        for symbol in operations:
            print(symbol)

        operation = input("What is the operation?: ")
        invalid_input = False

        for symbol in operation:
            if symbol not in "-+/*":
                invalid_input = True

    return operation

def get_rez(input_num1, input_operation, input_num2):
    num1 = input_num1
    operation = input_operation
    num2 = input_num2
    result = operations[operation](num1, num2)

    print(f"{num1} {operation} {num2} = {rez}")

    return result

rez = get_rez(get_number("1"), get_operation(), get_number("2"))

while True:
    calc_mode = input(f"Type 'y' to continue calculating with {rez}, or type 'n' to start a new calculation: ")
    if calc_mode == 'y':
        rez = get_rez(rez, get_operation(), get_number("2"))
    elif calc_mode == 'n':
        rez = get_rez(get_number("1"), get_operation(), get_number("2"))
    else:
        print("Invalid input.")
