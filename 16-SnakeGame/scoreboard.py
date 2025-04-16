from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self, score, high_score):
        super().__init__()
        self.penup()
        self.ht()
        self.color("white")
        self.goto(0, 275)
        self.update_scoreboard(score, high_score)

    def update_scoreboard(self, score, high_score):
        self.clear()
        self.write(f"Score: {score}, High Score: {high_score}", False, "center", ('Arial', 15, 'bold'))

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over.", False, "center", ('Arial', 15, 'bold'))

    def reset_scoreboard(self, score, high_score):
        if score > high_score:
            high_score = score
            with open("curr_record.txt", mode="w") as f:
                f.write(str(high_score))
        score = 0
        self.update_scoreboard(score, high_score)
        return high_score
