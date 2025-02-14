import random
import turtle
from random import choice
from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")

# ,,,,,,,,,,,,,,,,,,,,, Draw square ,,,,,,,,,,,,,,,,,,,,,,
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)
# ,,,,,,,,,,,,,,,,,,,,, Draw line with gaps ,,,,,,,,,,,,,,,,,,,,,,
# for i in range(15):
#         tim.up()
#         tim.forward(5)
#         tim.down()
#         tim.forward(5)
#

color = ["cyan", "orange", 'red', "green2", "yellow", 'maroon1', "purple1", 'OliveDrab1']
# ,,,,,,,,,,,,,,,,,,,,, Draw diff shape ,,,,,,,,,,,,,,,,,,,,,,
# for i in range(3, 10+1):
#     rotation = 360 / i
#     tim.pencolor(color[i-3])
#     for j in range(i):
#         tim.forward(100)
#         tim.left(rotation)


# ,,,,,,,,,,,,,,,,,,,,, Gender Random walk ,,,,,,,,,,,,,,,,,,,,,,

# possible direction
# up = 90
# down = 270
# left = 180
# right = 360
#
# direction = [up, down, left, right]
#
# # appearance
# tim.shape("circle")
# tim.width(10)
#
# # height and width of canvas
# height = 500
# width = 500
#
# # border
# minX, maxX = -width/2, width/2
# minY, maxY = -height/2, height/2
#
# # set speed of object
# tim.speed(100)
#
# # length of motion
# step = 20
#
#
# for _ in range(1000):
#     ban_direction = []
#
#     # capture impossible direction
#     if tim.xcor() - step < minX: ban_direction.append(left)
#     if tim.xcor() + step > maxX: ban_direction.append(right)
#     if tim.ycor() + step > maxY: ban_direction.append(up)
#     if tim.ycor() - step < minY: ban_direction.append(down)
#
#
#     next_head = choice(direction)
#     current_head = tim.heading()
#
#     # loop for find correct next step
#     switch = 1
#     while switch:
#         switch = 0
#         new_head = current_head + next_head
#
#         while new_head > 360:
#             new_head -= 360
#         for i in range(len(ban_direction)):
#             if new_head == ban_direction[i]:
#                 next_head = choice(direction)
#                 switch = 1
#
#     # set color
#     col = choice(color)
#     tim.color(col)
#     tim.pencolor(col)
#
#     # set direction and step
#     tim.left(next_head)
#     tim.forward(step)

# ,,,,,,,,,,,,,,,,,,,,, Gender Circle ,,,,,,,,,,,,,,,,,,,,,,

turtle.colormode(255)

def rgb_gender():
    r = random.randint(0 ,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rgb_tuple = (r, g, b)
    return rgb_tuple

tim.shape("classic")
# r = 100
# n = 40
# station = 360 / n
# tim.speed(100)
# for _ in range(n):
#     tim.color(rgb_gender())
#     tim.circle(r)
#     tim.left(station)

# ,,,,,,,,,,,,,,,,,,,,, Dot Art ,,,,,,,,,,,,,,,,,,,,,,


step = 40
w = 10
h = 30
tim.speed(100)
tim.width(20)
tim.up()
tim.setpos(-150, -150)
tim.down()
for _ in range(h):
    for _ in range(w):
        tim.pencolor(rgb_gender())
        tim.forward(0)
        tim.up()
        tim.forward(step)
        tim.down()


    tim.penup()
    tim.setpos(-150, tim.ycor() + step)
    tim.down()

tim.forward(0)
tim.up()
tim.forward(100)
tim.down()


tim.screen.mainloop()
