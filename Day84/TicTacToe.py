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

    def check_winner(self, player):
        if ((self.grid[0][0] == self.grid[0][1] == self.grid[0][2]) and self.grid[0][0] != BOX or
            (self.grid[1][0] == self.grid[1][1] == self.grid[1][2]) and self.grid[1][0] != BOX or
            (self.grid[2][0] == self.grid[2][1] == self.grid[2][2]) and self.grid[2][0] != BOX or
            (self.grid[0][0] == self.grid[1][0] == self.grid[2][0]) and self.grid[0][0] != BOX or
            (self.grid[0][1] == self.grid[1][1] == self.grid[2][1]) and self.grid[0][1] != BOX or
            (self.grid[0][2] == self.grid[1][2] == self.grid[2][2]) and self.grid[0][2] != BOX or
            (self.grid[0][0] == self.grid[1][1] == self.grid[2][2]) and self.grid[0][0] != BOX or
            (self.grid[0][2] == self.grid[1][1] == self.grid[2][0]) and self.grid[0][2] != BOX
            ):
            print(f"{player.name} is the winner!")
            player.add_score()
            print(f"Score: {player.name}: {player.score}")
            return True
        return False

class Player:
    def __init__(self, name, symbol):
        self.score = 0
        self.name = name
        self.symbol = symbol

    def add_score(self):
        self.score += 1
