# Bluprint - креслення

from turtle import Turtle, Screen

mayk = Turtle()


mayk.forward(100)
mayk.color("blue")

for steps in range(20):
    mayk.speed(500)
    for c in ('blue', 'red', 'green'):
        mayk.color(c)
        mayk.forward(steps)
        mayk.right(30)

jiny = Turtle()

# my_screen = Screen()
# my_screen.exitonclick()
# mayk.screen.mainloop()

