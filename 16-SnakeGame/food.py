from turtle import Turtle
from random import randint
LIMIT = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()

        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("blue")
        self.speed("fastest")

        x = randint(-LIMIT, LIMIT)
        y = randint(-LIMIT, LIMIT)
        self.goto(x, y)
