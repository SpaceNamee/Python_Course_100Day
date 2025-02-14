from turtle import Turtle, Screen
import random

screen = Screen()

#tim = Turtle()
# screen.listen()
#
# def move_forward():
#     tim.forward(20)
#
# def move_backward():
#     tim.backward(20)
#
# def move_counter_clockwise():
#     tim.left(50)
#
# def move_clockwise():
#     tim.right(1)
#
# screen.onkeypress(key="W", fun=move_forward)
# screen.onkeypress(key="S", fun=move_backward)
# screen.onkeypress(key="A", fun=move_counter_clockwise)
# screen.onkeypress(key="D", fun=move_clockwise)
# screen.exitonclick()

screen.setup(width=500, height=400)
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple' ]
position = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(6):
    new_item = Turtle(shape='turtle')
    new_item.penup()
    new_item.color(colors[i])
    new_item.goto(x=-230, y=position[i])
    all_turtle.append(new_item)

user_bat = screen.textinput(title="Make your bat", prompt='Which turtle will win the race? Enter a color: ')

start_racing = False
if user_bat != "":
    start_racing = True
while start_racing:
    rand_speed = []
    for i in range(6):
        rand_speed.append(random.randint(1, 10))

    for i in range(6):
        all_turtle[i].forward(rand_speed[i])
        if all_turtle[i].xcor() >= 220:
            if user_bat == all_turtle[i].color()[0]:
                print(f"You win! {user_bat} color win.")
            else:
                print(f"You loose! {all_turtle[i].color()[0]} color win, not {user_bat}")
            start_racing = False
            break
screen.exitonclick()