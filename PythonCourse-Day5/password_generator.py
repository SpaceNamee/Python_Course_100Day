import random

letters = ["q","w", "e", "r", "t","y", "u", "i", "o","p","a","s", "d", "f","g", "h", "j", "k","l", "z", "x", "c", "v", "b", "n","m", "Q", "W", "E", "R","T", "Y", "U","I","O","P","A", "S","D", "F ", "G", "H", "J","K","L","Z","X","C", "V","B","N","M"]
numbers = '1234567890'
symbols = "!@#$%^&*()_+=-?/.,<>][';:{}"

num_letters = int(input("How many letters would you want in your password?"))
num_numbers = int(input("How many numbers would you want in your password?"))
num_symbols = int(input("How many symbols would you want in your password?"))

length = num_symbols + num_letters + num_numbers
password = ""

while length:
    obj = random.randint(0,2)

    if obj == 0:
        if num_letters:
            password += letters[random.randint(0, len(letters) - 1)]
            num_letters -= 1
            length -= 1
    elif obj == 1:
        if num_numbers:
            password += numbers[random.randint(0, len(numbers) - 1)]
            num_numbers -= 1
            length -= 1
    elif obj == 2:
        if num_symbols:
            password += symbols[random.randint(0, len(symbols) - 1)]
            num_symbols -= 1
            length -= 1

print(password)