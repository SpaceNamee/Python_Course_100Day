from turtle import Turtle, Screen
from food import Food
from snake import Snake
from scoreboard import Score
import time

WIDTH = 600
HEIGHT = 600

screen = Screen()
screen.setup(width=WIDTH, height=600)
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
    if snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.ycor() > 280 or snake.head.xcor() < -280:
        game_is_on = 0

    # Detection collision with tall
    for part in snake.all_part[1:]:
         if snake.head.distance(part) < 10:
            game_is_on = False
            score.game_over()



screen.exitonclick()
