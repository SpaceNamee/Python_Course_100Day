# Отримати число перше
# Вибрати дію
# Отримати друге число
# Вивести результат

import art
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
        print("+ - / *")
        operation = input("What is the operation?: ")
        invalid_input = False
        for symbol in operation:
            if symbol not in "-+/*":
                invalid_input = True
    return operation

print(art.calc)
def calc(num1, num2, operation):
    rez = 0
    if operation == '+':
        rez = num1 + num2
    elif operation == "-":
        rez = num1 - num2
    elif operation == '*':
        rez = num1 * num2
    elif operation == '/':
        rez = num1 / num2

    print(f"{num1} {operation} {num2} = {rez}")
    return rez

def get_rez(input_num1, input_operation, input_num2):
    num1 = input_num1
    operation = input_operation
    num2 = input_num2
    return calc(num1, num2, operation)

rez = get_rez(get_number("1"), get_operation(), get_number("2"))
while True:
    calc_mode = input(f"Type 'y' to continue calculating with {rez}, or type 'n' to start a new calculation: ")
    if calc_mode == 'y':
        rez = get_rez(rez, get_operation(), get_number("2"))
    elif calc_mode == 'n':
        rez = get_rez(get_number("1"), get_operation(), get_number("2"))
    else:
        print("Invalid input.")



