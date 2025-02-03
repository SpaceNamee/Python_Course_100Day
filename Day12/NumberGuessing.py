from random import randint

import assci_art

print(assci_art.welcoming)
print("Guess the number. Number is between 1 to 1000")
start = 1
end = 1000
num = randint(start, end+1)
print(num)
while True:
    user_input = int(input("Enter number: "))
    diff = num - user_input
    if diff > 0:
        if diff > end / 2:
            print("Number is too small")
        else:
            print("Number is small")
    elif diff < 0:
        if -diff > end / 2:
            print("Number is too big")
        else:
            print("Number is big")
    else:
        print("You guess!")
        break


