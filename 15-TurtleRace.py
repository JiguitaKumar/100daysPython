from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

turtle_list = []
colors = ["purple", "blue", "green", "yellow", "orange", "red"]
pos_y = 50
pos_x = -240

for n in range(6):
    turtle_list.append(Turtle(shape="turtle"))
    turtle = turtle_list[n]

    turtle.color(colors[n])
    turtle.penup()
    turtle.goto(pos_x, pos_y)

    pos_y = pos_y - 20

if user_bet:
    run_is_on = True
    winner = ""

    while run_is_on:
        for turtle in turtle_list:
            steps = randint(0, 10)
            turtle.forward(steps)

            if turtle.position()[0] > 225:
                run_is_on = False
                winner = turtle.color()[0]
                print(f"The winner is {winner}!")

    if winner == user_bet:
        print("Your bet was correct! Congrats 🥳")
    else:
        print("Your bet was wrong ☹️. Better luck next time...")

screen.exitonclick()
