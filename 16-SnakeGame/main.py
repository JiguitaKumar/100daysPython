import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
food = Food()

score = 0
with open("curr_record.txt") as f:
    high_score = int(f.read())
scoreboard = Scoreboard(score, high_score)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


while True:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if not snake.check_position():
        high_score = scoreboard.reset_scoreboard(score, high_score)
        score = 0
        snake.reset()

    #detect colision with food
    if snake.head.distance(food) < 15:

        #update score
        score += 1
        scoreboard.update_scoreboard(score, high_score)

        #increase snakesize
        snake.add_square(snake.tail.xcor(), snake.tail.ycor())

        #delete current food and create new food
        food.ht()
        food = Food()
