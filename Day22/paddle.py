from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_position):
        super().__init__()
        self.setx(x_position)
        self.shape("square")
        self.color("white")
        self.up()
        self.setheading(-90)
        self.shapesize(1.0, 5.0)

    def move_forward(self):
        self.forward(10)

    def move_backward(self):
        self.backward(10)

