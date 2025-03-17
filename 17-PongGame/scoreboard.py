from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, left_score, right_score):
        super().__init__()
        self.score_update(left_score, right_score)

    def default_setup(self, score, y_coord):
        self.ht()
        self.penup()
        self.color("white")
        self.goto(y_coord, 250)
        self.write(score, False, "center", ("Trebuchet MS", 30, "bold"))

    def score_update(self, left_score, right_score):
        self.clear()
        self.default_setup(right_score, 30)
        self.default_setup(left_score, -30)
