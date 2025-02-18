import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.title("The turtle crossing capstone")
screen.listen()
screen.onkeypress(player.move, "Up")

cars_manager = CarManager()
score = Scoreboard()

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    cars_manager.create_car()
    cars_manager.move_car()

    if cars_manager.touch_with_player(player):
        score.game_over()
        game_is_on = False

    if player.ycor() == player.finish_line_y:
        player.player_reset()
        cars_manager.move_dist += cars_manager.move_increment
        score.level_up()

    screen.update()

screen.exitonclick()