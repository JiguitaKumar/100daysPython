from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, score):
        super().__init__()

        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard(score)

    def update_scoreboard(self, score):
        self.clear()
        self.write(f"Score: {score}", False, "center", ('Arial', 15, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", False, "center", ('Arial', 15, 'bold'))
