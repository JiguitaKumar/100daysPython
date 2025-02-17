from turtle import Turtle


class Line(Turtle):

    def __init__(self, y_coord):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(0.8, 0.1)
        self.goto(0, y_coord)
