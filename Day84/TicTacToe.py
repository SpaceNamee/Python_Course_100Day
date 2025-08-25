from ascii_art import BOX, CROSS_BOX, ZERO_BOX, LINE_H, ORDER_NUM

class TicTacToe:
    def __init__(self):
        self.grid = [[BOX, BOX, BOX], [BOX, BOX, BOX], [BOX, BOX, BOX]]     
        self.draw()
    
    def draw(self, positin=None, symbol=None):
        if positin and symbol is not None:
            row = (positin - 1) // 3
            col = (positin - 1) % 3
            
            if symbol == 'X':
                self.grid[row][col] = CROSS_BOX
            else:
                self.grid[row][col] = ZERO_BOX

        for row, order_num in zip(self.grid, ORDER_NUM):
            for f,s,th in zip(row[0], row[1], row[2]):
                print(f + "   " + s + "   " + th)
            print(order_num)

        print(LINE_H)

    def equals3(self, a, b, c):
        return a == b and b == c and a != BOX

    def check_winner(self):
        winner = None

        # Check horizontal
        for i in range(3):
            if self.equals3(self.grid[i][0], self.grid[i][1], self.grid[i][2]):
                winner = self.grid[i][0]

        # Check Vertical
        for i in range(3):
            if (self.equals3(self.grid[0][i], self.grid[1][i], self.grid[2][i])):
                winner = self.grid[0][i]

        # Check diagonals
        if (self.equals3(self.grid[0][0], self.grid[1][1], self.grid[2][2])):
            winner = self.grid[0][0]

        if (self.equals3(self.grid[2][0], self.grid[1][1], self.grid[0][2])):
            winner = self.grid[2][0]

        openSpots = 0;
        for i in range(3):
          for j in range(3):
            if (self.grid[i][j] == BOX):
                openSpots += 1

        if winner is None and openSpots == 0:
            return "tie"
        elif winner is not None:
            winner = "X" if winner == CROSS_BOX else "O"
            return winner
        else:
            return None
        

class Player:
    def __init__(self, name, symbol):
        self.score = 0
        self.name = name
        self.symbol = symbol
        self.is_ai = False
        self.symbol_art = ZERO_BOX if symbol == "0" else CROSS_BOX

    def add_score(self):
        self.score += 1




class AIPlayer(Player):
    def __init__(self, symbol):
        super().__init__(name="Computer", symbol=symbol)
        self.is_ai = True
        self.scores = {
              "X": 10,
              "O": -10,
              "tie": 0
            };

    def minimax_algorithm(self, board, depth, is_maximizing):
        res = board.check_winner()
        if res is not None:  # "X", "O", or "tie"
            return self.scores[res]

        if is_maximizing:
            best_score = -float('inf')
            for i in range(3):
                for j in range(3):
                    if board.grid[i][j] == BOX:
                        board.grid[i][j] = self.symbol_art  # AI move
                        score = self.minimax_algorithm(board, depth + 1, False)
                        board.grid[i][j] = BOX
                        best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            opponent_symbol = ZERO_BOX if self.symbol_art == CROSS_BOX else CROSS_BOX
            for i in range(3):
                for j in range(3):
                    if board.grid[i][j] == BOX:
                        board.grid[i][j] = opponent_symbol  # Opponent move
                        score = self.minimax_algorithm(board, depth + 1, True)
                        board.grid[i][j] = BOX
                        best_score = min(score, best_score)
            return best_score


    
    def best_move(self, board):
        best_score = -float('inf')
        pos = 0
        best_position = 0
        for i in range(0, 3):
            for j in range(0, 3):
                print("Position:", pos)
                pos += 1
                if board.grid[i][j] == BOX:
                    board.grid[i][j] = self.symbol_art
                    score = self.minimax_algorithm(board, 0, False)
                    print(score)
                    board.grid[i][j] = BOX
                    if score > best_score:
                        best_score = score
                        best_position = pos 
        print("Best Position: ##########################", best_position)


        return best_position