from paddle import Paddle
from turtle import Screen
from ball import Ball
from scoreborad import Score
import time

WIDTH = 800
HEIGHT = 600

#TODO
# Step 1: Create screen
screen = Screen()
screen.tracer(0)
screen.setup(width=WIDTH, height=HEIGHT)
screen.bgcolor("black")
screen.title("Pong")

#TODO
# Step 2: Create and move a paddle
# Step 3: Create another paddle
r_paddle = Paddle(350)
l_paddle = Paddle(-350)

#TODO
# Step 4: Create the ball and make ot move
ball = Ball()

#TODO
# Step 8: Keep score
score = Score()

screen.listen()

screen.onkeypress(r_paddle.move_forward, "Left")
screen.onkeypress(r_paddle.move_backward, "Right")

screen.onkeypress(l_paddle.move_forward, "d")
screen.onkeypress(l_paddle.move_backward, "a")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#TODO
# Step 5: Detect collision with wall and bounce
    if ball.ycor() > HEIGHT/2 - 20 or ball.ycor() < -HEIGHT/2 + 20:
        ball.bounce_y()

#TODO
# Step 6: Detect collision with paddle
    if ball.distance(r_paddle) <= 50 and ball.xcor() > 300 or ball.distance(l_paddle) <= 50 and ball.xcor() < -300:
        ball.bounce_x()

#TODO
# Step 7: Detect when paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()