from numpy import random
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
    "A" : 10
}
suits = ["Spades","Hearts" ,"Diamonds", "Clubs" ]
cards = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
"""Піка, Черва. Бубна, Хреста"""

def hand_out_card(dib=0):
    player_dip = [dib]
    player_cards = list(random.randint(len(cards), size=2))
    player_cards_suits = list(random.randint(len(suits), size=2))
    player  = [player_dip, player_cards, player_cards_suits]
    return player
"""Players отримують карти"""

def print_cards(player, name, mode=0):
    print()
    print(f"{name}:")
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


def is_blackjack(player):
    if (cards[player[1][0]] == "A" and cards_value[cards[player[1][1]]] == 10) or (cards[player[1][1]] == "A" and cards_value[cards[player[1][0]]] == 10):
        print("\nPLayer: WIN")
        print("Dealer: LOOSE")
        return True


def hit(player):
    player[1].append(random.randint(len(cards)))
    player[2].append(random.randint(len(suits)))


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

            if stay(player_1, dealer):
                balance += bid
            else:
                balance -= bid

            continue_round = False
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
    player_bid = int(input("Enter bid: "))
    player_balance = play_round(player_bid, player_balance)
    print(f"Balance: {player_balance}")
    check_continue = input("Continue? (yes/no): ")
    if check_continue == "no":
        break

