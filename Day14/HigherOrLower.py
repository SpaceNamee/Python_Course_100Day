import ascii_art
from game_data import data

print(ascii_art.logo)
score = 0
start = True
while start:
    for i in range(2, len(data) - 1):
        # print a comparable statement in different way that is up to starting game or not
        print("_______________________________________________________________________________________________________________")

        if score:
            print(f"\nCompare A: {data[i]["name"]}, {data[i]["description"]}, from {data[i]["country"]}, with {data[i]["follower_count"]}M followers")
        else:
            print(f"\nCompare A: {data[1]["name"]}, {data[1]["description"]}, from {data[1]["country"]}")

        print(ascii_art.vs)

        print(f"Against B: {data[i+1]["name"]}, {data[i+1]["description"]}, from {data[i+1]["country"]}")

        print("_______________________________________________________________________________________________________________")
        # Ask the player's answer
        while True:
            user_input = input("Who has more followers in millions (A or B)? ")

            if user_input == 'A' or  user_input == 'B':
                break

        # Define a true answer
        answer = 'B'
        if data[i]["follower_count"] > data[i+1]["follower_count"] : answer = 'A'

        # Compare true answer with player's answer
        if  user_input == answer:
            score += 1
            print(f"New score: {score}")
        else:
            print("You loose.")
            print(f"Your score: {score}")
            start = False
            break

