import colorgram as c
import turtle as t
import random

#get color palette
color_palette = c.extract("./dhs3823_0_1280_0-1024x958.jpg", 20)
colorList = []
for color in color_palette:
    temp_list = list(color.rgb)
    new_tuple = tuple(temp_list)
    colorList.append(new_tuple)

#create cursor and change color mode
pointer = t.Turtle()
#t.colormode(255)
pointer.speed(10)

#create screen
screen = t.Screen()
screen.exitonclick()

#initial position
pointer.penup()
pointer.setposition(-100, -100)
pointer.hideturtle()

def draw_line():
    for _ in range(10):
        pointer.dot(20, random.choice(colorList))
        pointer.forward(25)

def create_new_line():
    pointer.left(90)
    pointer.forward(25)
    pointer.left(90)
    pointer.setx(-100)
    pointer.right(90)
    pointer.right(90)

for _ in range(10):
    draw_line()
    create_new_line()
