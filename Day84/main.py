from TicTacToe import TicTacToe, Player, AIPlayer


def run(player_1, player_2):
    game = TicTacToe()
    
    turn = 0
    while True:
        current_player = player_1 if turn % 2 == 0 else player_2
        if current_player.is_ai:
            # AI logic to choose position
            
            position = current_player.best_move(game)
            game.draw(position, current_player.symbol)
        else:
            position = int(input(f"{current_player.name} - {current_player.symbol}, enter your position (1-9): "))
            game.draw(position, current_player.symbol)

 
        win = game.check_winner()
        if win == "tie":
            print("It's a tie!")
            break
        elif win in ["X", "O"]:
            winner = player_1 if player_1.symbol == win else player_2
            winner.add_score()
            print(f"{winner.name} wins!")
            print(f"Scores: {player_1.name} - {player_1.score}, {player_2.name} - {player_2.score}")
            break
        
        turn += 1

def new_game(ai=False):
    if ai:
        player_symbol = input("Choose your symbol [O/X]: ").upper()
        if player_symbol == "O":
            computer_symbol = "X"
        else:
            computer_symbol = "O"

        player_1 = Player(name=input(f"Enter name for Player 1 ({player_symbol}): "), symbol=player_symbol)
        player_2 = AIPlayer(symbol=computer_symbol)
    else:
        player_1 = Player(name=input("Enter name for Player 1 (O): "), symbol='O')
        player_2 = Player(name=input("Enter name for Player 2 (X): "), symbol='X')

    run(player_1, player_2) 
    
    return [player_1, player_2]

def start_game():
    opponent = input("Do you want to play against [computer - 1] or [friend - 2]? : ").lower()
    if opponent == "1":
        players = new_game(ai=True)
    else:
        players = new_game()


    while True:
        option_game = input("Do you want to [continue playing - 1], [start new game -2] or [exit - 3] ?: ").lower()
        if option_game  == "3":
            print("Thanks for playing!")
            break
        elif option_game == "2":
            players = start_game()
        elif option_game == "1":
            run(players[0], players[1])


if __name__ == "__main__":
    start_game()