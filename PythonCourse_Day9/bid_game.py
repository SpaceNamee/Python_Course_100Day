import re
# from PythonCourse_Day9 import art
import art
print(art.welcoming)

def find_highst_bidder(bidder):
    max = 0
    winner = 'noone'
    for key in bidder:
        if bidder[key] > max:
            max = bidder[key]
            winner = key
        elif bidder[key] == max:
            winner += " " + key
    print(f"Winner: {winner} bid: {max}")

bidder = {}
turn = True

while turn:
    name = input("Enter your name: ")
    bid = input("Enter your bid in $: ")
    if re.search("[a-z]", bid) != None :
        print("Invalid input")
        continue
    bidder[name] = int(bid)
    while True:
        another_bidder = input("There is another bidder? (yes, no): ").lower()
        if another_bidder == "no":
            find_highst_bidder(bidder)
            turn = False
            break
        elif another_bidder == "yes":
            print('\n' * 1000)
            break
        else:
            print("Invalid input.")

