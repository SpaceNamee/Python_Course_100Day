from numpy import random
import re
# Роздаю карти
# обераю опцію Hit, stand, split
# Розкриваю карти dealer's і обраховую
# додаю карти за потреби
# Результат

cards_value = {
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "10" : 10,
    "J" : 10,
    "Q" : 10,
    "K" : 10,
    "A" : 11
}
suits = ["Spades","Hearts" ,"Diamonds", "Clubs" ]
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
"""Піка, Черва. Бубна, Хреста"""



# def check_pairs():

def hand_out_card(dib=0):
    numbers = find_match_card()

    player_cards = [numbers[0]]
    player_cards_suits = [numbers[1]]

    numbers = find_match_card()

    player_cards.append(numbers[0])
    player_cards_suits.append(numbers[1])

    #
    player_dip = [dib]
    # player_cards = list(random.randint(len(cards), size=2))
    # player_cards_suits = list(random.randint(len(suits), size=2))
    #
    # while True:
    #     if player_cards[0] == player_cards[1] and player_cards_suits[0] == player_cards_suits[1]:
    #         player_cards[1] = random.randint(len(cards))
    #         player_cards_suits[1] = random.randint(len(suits))
    #     else:
    #         break
    #
    # is_using_pairs.append(player_cards)
    # is_using_pairs.append(player_cards_suits)
    player  = [player_dip, player_cards, player_cards_suits]
    return player
"""Players отримують карти"""

def print_cards(player, name, mode=0):
    print()
    print(f"{name}:")
    step = 0
    # while step <= len(player) - 1:
    #         for j in range(len(player[step+1]) - mode):
    #             print(cards[player[step+1][j]] + " " + suits[player[step+2][j]])
    #         step += 3

    for i in range(len(player[1]) - mode):
        print(cards[player[1][i]] + " " + suits[player[2][i]])


    score = calc_score(player, mode)
    print(f"Score: {score}")


def calc_score(player, mode=0):
    score = 0
    for i in range(len(player[1]) - mode):
        if cards[player[1][i]] == "A":
            if score + cards_value[cards[player[1][i]]] > 21:
                score += 1
                continue
        score += cards_value[cards[player[1][i]]]
    return score

def get_num(prompt):
    while True:
        a = input(prompt)
        if re.search('^[0-9]+$', a) is not None:
            break
    return a

def is_blackjack(player):
    if (cards[player[1][0]] == "A" and cards_value[cards[player[1][1]]] == 10) or (cards[player[1][1]] == "A" and cards_value[cards[player[1][0]]] == 10):
        print("\nPLayer: WIN")
        print("Dealer: LOOSE")
        return True

def find_match_card():
    switch = True
    a = random.randint(len(cards))
    b = random.randint(len(suits))
    while switch:
        switch = False

        for i in range(len(is_using_pairs[1])):
            if is_using_pairs[0][i] == a and is_using_pairs[1][i] == b:
                switch = True

                a = random.randint(len(cards))
                b = random.randint(len(suits))
    is_using_pairs[0].append(a)
    is_using_pairs[1].append(b)

    return [a,b]

def hit(player):
    numbers = find_match_card()

    player[1].append(numbers[0])
    player[2].append(numbers[1])
    # player[1].append(random.randint(len(cards)))
    # player[2].append(random.randint(len(suits)))


def is_over_21(player):
    if calc_score(player) > 21:
        print("\nYou: LOOSE")
        print("Dealer: WIN")
        return True
    return False


def stay(player, dealer):
    score_dealer = calc_score(dealer)
    score_player = calc_score(player)
    print_cards(dealer, "Dealer")
    print_cards(player, "Player_1")

    while True:
        if score_dealer < 17:
            hit(dealer)
            score_dealer = calc_score(dealer)
            print_cards(dealer, "Dealer")
            print_cards(player, "Player_1")
        else:
            break

    if score_dealer > 21 or score_dealer < score_player:
        print("\nYou: WIN")
        print("Dealer: LOOSE")
        return True
    elif score_dealer > score_player:
        print("\nDealer: WIN")
        print("You: LOOSE")
        return False
    elif score_dealer == score_player:
        print("\nDraw")
        return None

def split(player :list, balance):
    cards_hand_2 = player[1].pop()
    cards_suit_hand_2 = player[2].pop()

    reminder = player[0] % 2
    if reminder:
        player[0] -= reminder
        balance += reminder

    splitting_balance = player[0] / 2
    player[0] = splitting_balance

    player.append([splitting_balance])
    player.append(cards_hand_2)
    player.append(cards_suit_hand_2)

    return balance

# Цикл однієї гри
def play_round(bid, balance):
    continue_round = True

    player_1 = hand_out_card(100)
    dealer = hand_out_card()
    print_cards(dealer, "Dealer", 1)
    print_cards(player_1, "Player_1")
    if is_blackjack(player_1):
        continue_round = False
        balance += bid

    while continue_round:
        print()
        if player_1[1][0] == player_1[1][1]:
            player_input = input("Choose option 'hit', 'stay', 'split' or 'q' - exit: ")
        else:
            player_input = input("Choose option 'hit', 'stay' or 'q' - exit: ")

        if player_input == 'q':
            continue_round = False

        elif player_input == 'hit':
            hit(player_1)

            print_cards(dealer, "Dealer", 1)
            print_cards(player_1, "PLayer_1")

            if is_over_21(player_1):
                continue_round = False
                balance -= bid

        elif player_input == "stay":
            print_cards(dealer, "Dealer")
            print_cards(player_1, "PLayer_1")

            stage = stay(player_1, dealer)

            if stage:
                balance += bid
            elif stage is None:
                balance = balance
            else:
                balance -= bid
            continue_round = False
        elif player_input == "split":
            step = 0
            while step <= len(player_1):
                print_cards()
                if player_1[1][0] == player_1[1][1]:
                    player_input = input("Choose option 'hit', 'stay', 'split' or 'q' - exit: ")
                else:
                    player_input = input("Choose option 'hit', 'stay' or 'q' - exit: ")
        else:
            print("Invalid input.")

    return balance

start_game = True

while True:
    start = input("Start A New Game? (yes/no): ")

    if start == "no":
        start_game = False
        break
    elif start == "yes":
        start_game = True
        break
    else:
        print("Invalid input.")

player_balance = 1000

while start_game:

    player_bid = get_num("Enter dib: ")
    is_using_pairs = [[-1], [-1]]
    player_balance = play_round(player_bid, player_balance)
    print(f"Balance: {player_balance}")
    while True:
        check_continue = input("Continue? (yes/no): ")
        if check_continue == "no":
            start_game = False
            break
        elif check_continue == "yes":
            break
        else:
            print("Invalid input.")

