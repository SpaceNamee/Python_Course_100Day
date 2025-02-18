from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280



class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.setheading(90)
        self.setpos(STARTING_POSITION)
        self.finish_line_y = FINISH_LINE_Y

    def move(self):
        self.forward(MOVE_DISTANCE)

    def player_reset(self):
        self.setpos(STARTING_POSITION)
