from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.count = 0
        self.up()
        self.color("white")
        self.setpos(0, 240)
        self.write(f"Score: {self.count}", align='center', font=('Arial', 16, 'bold'))


    def counting(self):
        self.clear()
        self.count += 1
        self.write(f"Score: {self.count}", align='center', font=('Arial', 16, 'bold'))

    def game_over(self):
        self.setpos(0,0)
        self.write("Game over", align='center', font=('Arial', 16, 'bold'))

