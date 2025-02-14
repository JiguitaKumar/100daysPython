from turtle import Turtle
import time
MOVE_DISTANCE = 20
SCREEN_LIMIT = 295
INITIAL_SNAKE_SIZE = 3


class Snake:

    def __init__(self):
        self.snake = []
        x_init_pos = 0
        y_init_pos = 0
        for _ in range(INITIAL_SNAKE_SIZE):
            self.add_square(x_init_pos, y_init_pos)
            x_init_pos = x_init_pos - MOVE_DISTANCE
        self.head = self.snake[0]
        self.tail = self.snake[-1]

    def add_square(self, x_pos, y_pos):
        turtle = Turtle(shape="square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(x_pos, y_pos)
        self.snake.append(turtle)

    def move(self):
        initial_pos = self.snake[0].pos()
        for n in range(len(self.snake)):
            if n == 0:
                self.snake[n].forward(MOVE_DISTANCE)
            else:
                new_pos = self.snake[n].pos()
                self.snake[n].goto(initial_pos)
                initial_pos = new_pos

    def check_position(self):
        curr_x = self.head.xcor()
        curr_y = self.head.ycor()

        if round(curr_x, 0) == -0:
            curr_x = 0.00
        if round(curr_y, 0) == -0:
            curr_y = 0.00
        if curr_x > SCREEN_LIMIT or curr_y > SCREEN_LIMIT or curr_x < -SCREEN_LIMIT or curr_y < -SCREEN_LIMIT:
            return False

        for n in self.snake[1:]:
            if round(curr_x, 2) == round(n.xcor(), 2) and round(curr_y, 2) == round(n.ycor(), 2):
                return False

        return True

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def right(self):
        self.head.setheading(0)

    def left(self):
        self.head.setheading(180)
