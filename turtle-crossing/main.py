import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move_up, "Up")

scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    count = random.randint(1,4)

    #detecting collision with upper wall
    if player.ycor() >  280:
        player.move_origin()
        car_manager.level_up()
        scoreboard.increase_score()

    #creating cars randomly
    if count == 1:
        car_manager.generate()

    car_manager.move_x()

    #detect car collision with turtle

    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False


screen.exitonclick()