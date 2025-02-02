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



def hand_out_card(dib=0, balance =1000):
    player_cards = []
    player_cards_suits = []

    for i in range(2):
        numbers = find_match_card()

        player_cards.append(numbers[0])
        player_cards_suits.append(numbers[1])

    player_money = [dib, balance]
    player  = [player_money, player_cards, player_cards_suits]
    return player
"""Players отримують карти"""

def print_cards(player, name, mode=0):
    print()
    print(f"{name}:")

    if mode:mode =len(player[1]) - 1

    for i in range(len(player[1]) - mode):
        print(cards[player[1][i]] + " " + suits[player[2][i]])


    score = calc_score(player, mode)
    print(f"Score: {score}")

def calc_score(player, mode=0):
    score = 0
    count_a = 0
    for i in range(len(player[1]) - mode):
        if cards[player[1][i]] == "A":
            if score + cards_value[cards[player[1][i]]] > 21:
                count_a += 1
        score += cards_value[cards[player[1][i]]]

    while count_a and score > 21:
        score -= 10
        count_a -= 1

    return score

def get_num(prompt):
    while True:
        a = input(prompt)
        if re.search('^[0-9]+$', a) is not None:
            break
    return int(a)

def is_blackjack(player):
    return True if (cards[player[1][0]] == "A" and cards_value[cards[player[1][1]]] == 10) or (cards[player[1][1]] == "A" and cards_value[cards[player[1][0]]] == 10) else False

def find_match_card():
    global is_using_pairs
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

def is_over_21(player):
    if calc_score(player) > 21:
        return True

    return False


def stay(player, dealer, dib, balance, players_stage):
    score_dealer = calc_score(dealer)
    score_player = calc_score(player)

    while True:
        if score_dealer < 17:
            hit(dealer)
            score_dealer = calc_score(dealer)
        else:
            break

    if score_dealer > 21 or score_dealer < score_player:
        balance += dib
        players_stage.append(True)
    elif score_dealer > score_player:
        balance -= dib
        players_stage.append(False)
    elif score_dealer == score_player:
        players_stage.append(None)

    return balance


def condition_split_or_double_down(player :list):
    return False if len(player[1]) != 2 else True

def split(player :list):
    player = [
        [[player[0][0], player[0][1]], [player[1][0]], [player[2][0]]],
        [[player[0][0], player[0][1]], [player[1][1]], [player[2][1]]]
    ]

    return player

def double_down(player):
    player[0][0] *= 2
    return player[0][0]


def play(player, dealer, players_stage, ace_exception=False):
    global name
    continue_round = True

    dib = player[0][0]
    balance = player[0][1]

    if len(player[1]) == 2:
        if is_blackjack(player):
            continue_round = False
            if is_blackjack(dealer):
                players_stage.append(None)
            else:
                players_stage.append(True)
                balance += dib * 1.5

            print("BLACKJACK!!!")

    while continue_round:
        print()
        if len(player[1]) == 2:
            if cards_value[cards[player[1][0]]] == cards_value[cards[player[1][1]]]:
                player_input = input("Choose option 'hit', 'stay', 'double down', 'split' or 'q' - exit: ")
            else:
                player_input = input("Choose option 'hit', 'stay', 'double down' or 'q' - exit: ")
        else:
            player_input = input("Choose option 'hit', 'stay', 'double down' or 'q' - exit: ")

        if player_input == 'q':
            players_stage.append(False)
            balance -= dib
            continue_round = False

        elif player_input == 'hit':

            hit(player)

            print_cards(player, name)

            if ace_exception:
                balance = stay(player, dealer, dib, balance, players_stage)
                break

            if is_over_21(player):
                players_stage.append(False)
                balance -= dib
                break

        elif player_input == "stay":
            balance = stay(player, dealer, dib, balance, players_stage)
            break

        elif player_input == "split":

            if not condition_split_or_double_down(player):
                print("Split is impossible.")
                continue

            if "Hand" in name:
                a = name[len(name) - 1]
                name = name[:len(name)] +name[len(name) - 1].replace(a, f"{int(a) - 1}")

            player = split(player)
            print_cards(dealer, "Dealer", 1)

            balance_hands = 0
            ace_exception = False
            if player[0][1][0] == player[1][1][0] and cards[player[1][1][0]] == "A":
                ace_exception = True
            for i in range(len(player)):
                if " Hand " not in name:
                    name += " Hand 0"
                index_hand = name[len(name) - 1]
                name = name.replace(index_hand, f"{int(index_hand) + 1}")
                print_cards(player[i], f"{name}")

                balance_hands += play(player[i], dealer, players_stage, ace_exception) - balance

            balance += balance_hands
            break

        elif player_input == "double down":
            if not condition_split_or_double_down:
                print("Double downing is impossible")
                continue
            dib = double_down(player)

            hit(player)

            print_cards(player, name)

            balance = stay(player, dealer, dib, balance, players_stage)
            continue_round = False
        else:
            print("Invalid input.")

    player[0][1] = balance
    return balance

def view_win_rate(win_rate):
    for i in range(len(win_rate)):
        print("________________________________")
        print(f"\n{name} {i + 1}")

        for j in range(len(win_rate[i])):

            if len(win_rate[i]) != 1:
                print(f"{name} Hand {j + 1}")
            if win_rate[i][j]:
                print("You: WIN")
                print("Dealer: LOOSE")
            elif win_rate[i][j] is None:
                print("Draw")
            else:
                print("You: LOOSE")
                print("Dealer: WIN")

        print("________________________________")


name = "Player"
# Цикл однієї гри
def play_round(num_players, balances, dibs):
    dealer = hand_out_card()

    global name

    win_rate = []
    current_balance = balances
    new_balance = []

    for i in range(0,num_players):
        player_1 = hand_out_card(dibs[i], current_balance[i])

        print_cards(dealer, "Dealer", 1)
        name = f"{name}" + f" {i+1}"
        print_cards(player_1, name)

        rate = []
        new_balance.append(play(player_1, dealer, rate))
        win_rate.append(rate)
        name = "Player"

        print("______________________________________")

    print_cards(dealer, "Dealer")

    view_win_rate(win_rate)

    return new_balance

def print_balance(balances):
    is_zero = False
    for i in range(len(balances)):
        if balances[i] == 0:
            is_zero = True
        print(f"{name} {i+1}: {balances[i]}")

    return is_zero

# цикл гри
is_using_pairs = []

def game_cycle(start_game, num_player, balance):
    while start_game:
        global is_using_pairs
        is_using_pairs = [[-1], [-1]]

        print(f"Current Balance: ")
        print_balance(balance)

        player_bid = []
        for i in range(num_player):
            while True:
                input_dib = get_num(f"Enter {name}'s {i + 1} dib: ")

                if input_dib > balance[i]:
                    print(f"{input_dib} is bigger than your balance({balance[i]})")
                    continue
                player_bid.append(input_dib)
                break
        balance = play_round(num_player, balance, player_bid)

        print(f"New Balance: ")
        print_balance(balance)

        while True:
            check_continue = input("Continue? (yes/no): ")
            if check_continue == "no":
                start_game = False
                break
            elif check_continue == "yes":
                break
            else:
                print("Invalid input.")

while True:
    start = input("Start A New Game? (yes/no): ")

    if start == "no":
        break
    elif start == "yes":
        number_of_players = 0
        while True:
            a = get_num("Number of players: ")
            if a > 1:
                number_of_players = a
                break
            else:
                continue
        players_balance = [1000 for i in range(number_of_players)]
        game_cycle(True, number_of_players, players_balance)
    else:
        print("Invalid input.")
