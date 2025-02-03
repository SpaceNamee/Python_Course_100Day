import numpy.random

import ascii_art
from game_data import data
import random

def print_comparable_statement(i):
    """print a comparable statement in different way that is up to starting game or not"""
    print(
        "_______________________________________________________________________________________________________________")
    if score:
        obj_a = used_num[i]
        print(
            f"\nCompare A: {data[obj_a]["name"]}, {data[obj_a]["description"]}, from {data[obj_a]["country"]}, with {data[obj_a]["follower_count"]}M followers")
    else:
        obj_a = random.randint(0, len(data))
        print(
            f"\nCompare A: {data[obj_a]["name"]}, {data[obj_a]["description"]}, from {data[obj_a]["country"]}, with {data[obj_a]["follower_count"]}M followers")

    print(ascii_art.vs)

    while True:
        obj_b = random.randint(0, len(data))
        if obj_b != obj_a:
            break

    print(
        f"Against B: {data[obj_b]["name"]}, {data[obj_b]["description"]}, from {data[obj_b]["country"]}, with {data[obj_b]["follower_count"]}M followers")

    print(
        "_______________________________________________________________________________________________________________")

    return [obj_a, obj_b]

print(ascii_art.logo)
score = 0
start = True
# Initialize array with first value which never be use but will save my structure with if score
used_num = [-1]
while start:
    for i in range(0, len(data)):

        # get objects = [obj_a, obj_b]
        objects = print_comparable_statement(i)
        obj_a = objects[0]
        obj_b = objects[1]

        # Ask the player's answer
        while True:
            user_input = input("Who has more followers in millions (A or B)? ").upper()

            if user_input == 'A' or  user_input == 'B':
                break

        # Define a true answer
        answer = 'B'
        if data[obj_a]["follower_count"] > data[obj_b]["follower_count"] : answer = 'A'

        # Compare true answer with player's answer
        if  user_input == answer:
            score += 1

            if user_input == 'A':
                used_num.append(obj_a)
            else:
                used_num.append(obj_b)

            print(f"New score: {score}")
        else:
            print("You loose.")
            print(f"Your score: {score}")
            start = False
            break

