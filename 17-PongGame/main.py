from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from line import Line
from scoreboard import Scoreboard
import time

# screen setup
screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# create mid-line
y = 275
while y > -280:
    line = Line(y)
    y = y - 30

# paddles creation
x_coordinate = 350
right_paddle = Paddle(x_coordinate)
left_paddle = Paddle(-x_coordinate)

#screen.update()
#screen.tracer(1)
screen.listen()
# make the screen listen - right paddle
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

# make the screen listen - left paddle
screen.onkey(left_paddle.up, "a")
screen.onkey(left_paddle.down, "z")

# create the ball
ball = Ball()

# create score
right_player_score = 0
left_player_score = 0
right_player_scoreboard = Scoreboard(right_player_score, 30)
left_player_scoreboard = Scoreboard(left_player_score, -30)

game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move(right_paddle, left_paddle)

screen.exitonclick()
