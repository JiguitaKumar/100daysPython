from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()
        self.create_score(score)

    def create_score(self, score):
        self.ht()
        self.penup()
        self.goto(-250, 265)
        self.write(f"Score: {score}", False, "left", FONT)
        self.color("black")

    def update_scoreboard(self, curr_score):
        self.clear()
        self.create_score(curr_score)

    def end_game_msg(self):
        self.clear()
        self.ht()
        self.penup()
        self.goto(0, 0)
        self.write(f"Game Over.", False, "center", FONT)
        self.color("black")
