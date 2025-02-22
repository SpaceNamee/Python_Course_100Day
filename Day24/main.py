from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Score
import time

file = open("text.txt")


WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()
    time.sleep(0.1)

    # Detect collision with food
    if food.distance(snake.head) < 15:
        food.refresh()
        snake.extend()
        score.counting()

    # Detect collision with wall
    if snake.head.xcor() >= 290 or snake.head.ycor() <= -290 or snake.head.ycor() >= 290 or snake.head.xcor() <= -290:
        screen.update()
        print(snake.head.xcor())
        print(snake.head.ycor())
        snake.reset()
        score.reset_scoreboard()


    # Detection collision with tall
    for part in snake.all_part[1:]:
         if snake.head.distance(part) < 10:
            score.reset_scoreboard()
            snake.reset()
            snake.create_snake()

screen.exitonclick()
