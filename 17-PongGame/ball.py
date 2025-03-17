from turtle import Turtle
from random import randint
from paddle import Paddle
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.seth(randint(-75, 75) + 180 * randint(0,1))
        self.move_speed = 0.05
        print(self.heading())

    def wall_collision(self):
        curr_dir = self.heading()
        if self.ycor() < -280 or self.ycor() > 280:
            self.seth(curr_dir * -1)

    def paddle_collision(self, paddle: Paddle):
        curr_dir = self.heading()
        if (abs(self.xcor() - paddle.xcor()) < 20) and (abs(self.ycor() - paddle.ycor()) < 45):
            self.seth(curr_dir - 180 - (self.ycor() - paddle.ycor()))
            return True

    def move(self, r_paddle: Paddle, l_paddle: Paddle):
        time.sleep(self.move_speed)
        print(self.move_speed)
        self.wall_collision()
        if self.paddle_collision(r_paddle) is True or self.paddle_collision(l_paddle) is True:
            self.move_speed = self.move_speed - 0.0025
        self.forward(10)

        if self.xcor() > 400:
            self.ht()
            return 1

        if self.xcor() < -400:
            self.ht()
            return -1
