import random

print(r'''
__        __   _                                 _               | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
\ \      / /__| | ___ ___  _ __ ___   ___       | |_ ___         | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \      | __/ _ \        |  _  | (_| | | | | (_| | | | | | | (_| | | | |
  \ V  V /  __/ | (_| (_) | | | | | |  __/      | || (_) |       |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
 _ \_/\_/ \___|_|\___\___/|_| |_| |_|\___|      \__\___/                |___/                             
''')

kitchen = ["table", "plate", "fork", "knife", "chair", "cup", "spoon", "pan", "cupboard", "bowl", "oven", "whisk"]
hangman = [r'''
  +---+
  |   |
      |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
fail_count = 0
word = kitchen[random.randint(0, len(kitchen) - 1)]
user_word = []
for i in range(len(word)):
    user_word.append('_')

while True:
    print(f"Fill {"".join(user_word)}")
    user_input = input("Enter letter: ")
    if len(user_input) == 1:
        if word.find(user_input) == -1:
            print(f"Your score {fail_count}/{len(hangman)}: {hangman[fail_count]}")
            if fail_count == len(hangman) - 1:
                print("You loose")
                break
            fail_count += 1
        else:
            start = word.find(user_input)
            while True:
                user_word[start] = word[start]
                start = word.find(user_input, start+1)
                if start == -1 or start == len(word) - 1:
                    break


    if word == "".join(user_word):
        print("You win!")
        break
