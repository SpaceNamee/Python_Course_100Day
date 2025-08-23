from TicTacToe import TicTacToe, Player


def run(player_1, player_2):
    game = TicTacToe()
    
    turn = 0
    while True:
        current_player = player_1 if turn % 2 == 0 else player_2
        positin = int(input(f"{current_player.name} - {current_player.symbol}, enter your position (1-9): "))
        game.draw(positin, current_player.symbol)

        win = game.check_winner(current_player)
        if win:
            break

        turn += 1

def new_game():
    player_1 = Player(name=input("Enter name for Player 1 (O): "), symbol='O')
    player_2 = Player(name=input("Enter name for Player 2 (X): "), symbol='X')

    run(player_1, player_2)
    
    return [player_1, player_2]

def start_game():
    players = new_game()
    while True:
        option_game = input("Do you want to [continue playing - 1], [start new game -2] or [exit - 3] ?: ").lower()
        if option_game  == "3":
            print("Thanks for playing!")
            break
        elif option_game == "2":
            players = new_game()
        elif option_game == "1":
            run(players[0], players[1])

if __name__ == "__main__":
    start_game()