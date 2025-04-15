import time
from random import randint
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

#create screen and personalize definitions
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#create player instance and its ability to move
player = Player()
screen.onkeypress(player.move, "Up")
screen.listen()

#create scoreboard and provide initial score
score = 0
scoreboard = Scoreboard(score)

#create car manager
car_manager = CarManager()

#game logic
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    #create cars and make them move
    car_manager.new_car()
    car_manager.move(score)

    #detect crashes
    for car in car_manager.cars:
        if (abs(car.ycor() - player.ycor())) < 25 and (abs(car.xcor() - player.xcor())) < 5:
            scoreboard.end_game_msg()
            screen.update()
            time.sleep(2)
            game_is_on = False

    #update soreboard, level and speed whenever turtle reaches end of the screen
    if player.next_level():
        score += 1
        scoreboard.update_scoreboard(score)
