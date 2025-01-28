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

num1 = get_number("1")
operation = get_operation()
num2 = get_number("2")
calc(num1, num2, operation)


