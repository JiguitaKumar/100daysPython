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
scoreboard = Scoreboard(score)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

can_move = True
while can_move:
    screen.update()
    time.sleep(0.1)
    snake.move()
    can_move = snake.check_position()

    #detect colision with food
    if snake.head.distance(food) < 15:

        #update score
        score += 1
        scoreboard.update_scoreboard(score)

        #increase snakesize
        snake.add_square(snake.tail.xcor(), snake.tail.ycor())

        #delete current food and create new food
        food.ht()
        food = Food()

scoreboard.game_over()
screen.exitonclick()
