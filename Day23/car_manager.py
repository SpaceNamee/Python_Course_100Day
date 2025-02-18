from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_dist = 5
        self.move_increment = 10

    def create_car(self):
        num_of_cars = random.randint(1, 6)
        if num_of_cars == 1:
            pos_y = random.randint(-230, 280)
            new_car = Turtle(shape="square")
            new_car.up()
            new_car.setpos(300, pos_y)
            new_car.shapesize(1, 2)
            color = random.randint(0,len(COLORS) - 1)
            new_car.color(COLORS[color])
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(20)
            if car.xcor() < -300:
                self.all_cars.remove(car)
                car.ht()

    def touch_with_player(self, player):
        for car in self.all_cars:
            if car.distance(player) <= 20 :
                return True

        return False

