from turtle import Turtle , Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen =Screen()
screen.setup(height= 600, width= 800)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(l_paddle.go_up, "w")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision with wall (UP AND DOWN)
    if ball.ycor() > 280 or ball.ycor() < -280 :
        #needs to bounce
        ball.bounce_y()

    #detetct collision with right paddle / r_paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect collision with walls(left and right)
    #right misses
    if ball.xcor() > 380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()

    #left misses
    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()
screen.exitonclick()