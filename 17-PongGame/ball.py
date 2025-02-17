from turtle import Turtle
from random import randint
from paddle import Paddle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.seth(randint(0, 360))

    def wall_collision(self):
        curr_dir = self.heading()
        if self.ycor() < -280 or self.ycor() > 280:
            self.seth(curr_dir * -1)

    def paddle_collision(self, paddle: Paddle):
        curr_dir = self.heading()
        if (abs(self.xcor() - paddle.xcor()) < 20) and (abs(self.ycor() - paddle.ycor()) < 30):
            print(curr_dir)
            self.seth(curr_dir - 180 - (self.ycor() - paddle.ycor()))
            print(self.heading())

    def move(self, r_paddle: Paddle, l_paddle: Paddle):
        self.wall_collision()
        self.paddle_collision(r_paddle)
        self.paddle_collision(l_paddle)
        self.forward(10)
