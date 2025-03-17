from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_cor):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(5, 1)
        self.goto(x_cor, 0)

    def up(self):
        if self.ycor() < 245:
            y = self.ycor() + 20
            self.goto(self.xcor(), y)

    def down(self):
        if self.ycor() > -240:
            y = self.ycor() - 20
            self.goto(self.xcor(), y)
