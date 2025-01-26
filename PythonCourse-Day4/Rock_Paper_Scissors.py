import itertools
import random

import IPython.core.debugger
option = ["""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", """
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""]

flag = True
print(r'''
                     _   _      _ _        __        __         _     _ _ 
                    | | | | ___| | | ___   \ \      / /__  _ __| | __| | |
                    | |_| |/ _ \ | |/ _ \   \ \ /\ / / _ \| '__| |/ _` | |
                    |  _  |  __/ | | (_) |   \ V  V / (_) | |  | | (_| |_|
                    |_| |_|\___|_|_|\___/     \_/\_/ \___/|_|  |_|\__,_(_)
''')
while flag:
    a = True
    player = input("Enter 0 - Rock, 1 - Paper, 2 - scissors or q - exit: ")
    computer = random.randint(0,2)
    while True:
        if player == 'q':
            flag = False
            break
        elif player == '1':
            print(f'''Your turn: {option[1]} \nComputer turn: {option[computer]}''')
            if computer == int(player):
                print("It is draw")
            elif computer == 0:
                print("You win")
            else:
                print("You loose")

            break
        elif player == '0':
            print(f'''Your turn: {option[0]} \nComputer turn: {option[computer]}''')
            if computer == int(player):
                print("It is draw")
            elif computer == 1:
                print("You loose")
            else:
                print("You win")
            break
        elif player == '2':
            print(f'''Your turn: {option[2]} \nComputer turn: {option[computer]}''')
            if computer == int(player):
                print("It is draw")
            elif computer == 1:
                print("You win")
            else:
                print("You loose")
            break

        else:
            player = input("Enter 0 - Rock, 1 - Paper, 2 - scissors or q - exit: ")
