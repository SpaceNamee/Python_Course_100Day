import re

print(r'''
 ____  _     _  
| __ )(_) __| | 
|  _ \| |/ _` | 
| |_) | | (_| | 
|____/|_|\__,_| 
''')
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
        another_bidder = input("There is another bidder? (yes, no): ")
        if another_bidder == "no":
            max = 0
            winner = 'noone'
            for key in bidder:
                if bidder[key] > max:
                    max = bidder[key]
                    winner = key
                elif bidder[key] == max:
                    winner += " " + key
            turn = False
            print(f"Winner: {winner} bid: {max}")
            break
        elif another_bidder == "yes":
            print('\n' * 1000)
            break
        else:
            print("Invalid input.")
