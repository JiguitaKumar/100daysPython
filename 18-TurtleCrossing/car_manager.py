from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []

    def new_car(self):
        if randint(0, 4) == 3:
            car = Turtle()
            car.shape("square")
            car.penup()
            car.shapesize(1, 2)
            car.color(COLORS[randint(0, len(COLORS)-1)])
            car.goto(280, randint(-230, 230))
            car.setheading(180)
            self.cars.append(car)

    def move(self, curr_score):
        for car in self.cars:
            if car.xcor() < -330:
                self.cars.remove(car)
            car.forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * curr_score)

