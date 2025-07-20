from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed= STARTING_MOVE_DISTANCE

    def generate(self):
        new_cars = Turtle()
        new_cars.shape("square")
        new_cars.color(random.choice(COLORS))
        new_cars.shapesize(stretch_wid=1, stretch_len=3)
        new_cars.penup()
        # new_cars.goto(320, random.randrange(-280 , 280, 10))
        random_y = random.randint(-250,250)
        new_cars.goto(300, random_y)
        self.all_cars.append(new_cars)
        # self.move_x()

    def move_x(self):
        for car in self.all_cars :
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT