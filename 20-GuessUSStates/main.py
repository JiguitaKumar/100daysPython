import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_dict = pandas.read_csv("50_states.csv").to_dict(orient='records')
states_list = [state['state'] for state in states_dict]
right_answers = 0
user_guess_list = []

while len(user_guess_list) < 50:
    user_guess = screen.textinput(title=f"{right_answers}/50 States Correct", prompt="What's another state name?").title()
    if user_guess in states_list and user_guess not in user_guess_list:
        user_guess_list.append(user_guess)
        right_answers += 1

        state_turtle = turtle.Turtle()
        state_turtle.ht()
        state_turtle.penup()

        for state in states_dict:
            if state['state'] == user_guess:
                state_turtle.goto(state['x'], state['y'])
                state_turtle.write(arg=user_guess, align="center", font=("Courier", 7, "normal"))

    if user_guess == "Exit":
        break

states_to_learn = []
for state in states_list:
    if state not in user_guess_list:
        states_to_learn.append(state)

with open("states_to_learn.csv", 'w') as f:
    states_to_learn_str = str(states_to_learn)
    f.write(states_to_learn_str)
