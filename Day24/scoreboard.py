from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.count = 0
        self.up()
        with open("text.txt") as file:
            self.high_score = file.read()
        self.color("white")
        self.setpos(0, 240)
        self.show()

    def reset_scoreboard(self):
        if self.count > int(self.high_score):
            self.high_score = self.count
            with open("text.txt", mode="w") as file:
                 file.write(str(self.high_score))
        self.count = 0
        self.show()

    def show(self):
        self.clear()
        self.write(f"Score: {self.count} High Score: {self.high_score}", align='center', font=('Arial', 16, 'bold'))

    def counting(self):
        self.count += 1
        self.show()

    # def game_over(self):
    #     self.setpos(0,0)
    #     self.write("Game over", align='center', font=('Arial', 16, 'bold'))

