from turtle import Turtle
import time

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MODE_DIST = 20

UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.all_part = []
        self.create_snake()
        self.head = self.all_part[0]

    def create_snake(self):
        for cor in STARTING_POSITION:
            self.add_part(cor)

    def reset(self):
        for part in self.all_part:
            part.goto(1000,1000)
        self.all_part.clear()
        self.create_snake()
        self.head = self.all_part[0]

    def add_part(self, position):
        new_part = Turtle(shape="square")
        new_part.color("white")
        new_part.penup()
        new_part.setpos(position)

        self.all_part.append(new_part)

    def extend(self):
        self.add_part(self.all_part[-1].position())

    def move(self):
        distX = 0
        distY = 0
        if self.head.xcor() + MODE_DIST > 290:
            distX = self.head.xcor() + MODE_DIST - 290
        if self.head.ycor() - MODE_DIST < -290:
            distY = self.head.ycor() - MODE_DIST + 290
        if self.head.ycor() + MODE_DIST > 290:
            distY = self.head.ycor() + MODE_DIST - 290
        if self.head.xcor() - MODE_DIST < -290:
            distX = self.head.xcor() - MODE_DIST + 290
        # print(f"Dist {dist}")
        if distX:
            for i in range(len(self.all_part)):
                new_x = self.all_part[i].xcor() + distX
                self.all_part[i].goto(new_x, self.all_part[i].ycor())
        elif distY:
            for i in range(len(self.all_part)):
                new_y = self.all_part[i].ycor() + distY
                self.all_part[i].goto(self.all_part[i].xcor(), new_y)
        else:
            for num_part in range(len(self.all_part) - 1, 0, -1):
                new_x = self.all_part[num_part - 1].xcor()
                new_y = self.all_part[num_part - 1].ycor()

                self.all_part[num_part].goto(new_x, new_y)

            self.head.forward(MODE_DIST)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


