from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, score, y_coord):
        super().__init__()
        self.ht()
        self.penup()
        self.color("white")
        self.goto(y_coord, 250)
        self.write(score, False, "center", ("Trebuchet MS", 30, "bold"))
