from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count = 0
        self.up()
        self.ht()
        self.setpos(-200, 250)
        self.write(f"Level {self.count}", align="center", font=FONT)

    def level_up(self):
        self.count += 1
        self.clear()
        self.write(f"Level {self.count}", align="center", font=FONT)

    def game_over(self):
        self.setpos(0,0)
        self.write(f"Game over", align="center", font=FONT)


