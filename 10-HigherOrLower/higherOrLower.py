from game_data import data
from art import logo, vs
from random import randint

def higherOrLower():
    #first print logo
    print(logo)

    #set up initial variables
    gameOn = True
    score = 0
    first_contender = data[randint(0, len(data)-1)]

    while gameOn:

        #get random data
        contenders = get_random_contenders(first_contender)
        first_contender = contenders[1]
        
        #ask for the user's input
        answer = game_logic(contenders)

        if answer:
           score += 1
           print(f"You are right! Current score: {score}. \n")
           print(" \n-----------------------//----------------------- \n")

        else:
            print(f"\nSorry, that's wrong. Final score: {score}.")
            gameOn = False
        

#get a different second element for the list
def get_random_contenders(first_contestant):
    second_contestant = data[randint(0, len(data)-1)]
    
    while first_contestant == second_contestant:
        second_contestant = data[randint(0, len(data)-1)]
    
    print(f"Compare A: {format_text(first_contestant)}.")
    print(vs)
    print(f"Against B: {format_text(second_contestant)}.")
    
    return [first_contestant, second_contestant]


#game logic
def game_logic(data):

    right_answer = ""
    if data[0]["follower_count"] > data[1]["follower_count"]:
        right_answer = "A"
    else:
        right_answer = "B"

    guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()

    if guess == right_answer:
        return True
    else:
        return False


#format contestant info
def format_text(contestant):
    name = contestant["name"]
    description = contestant["description"] 
    country = contestant["country"]

    return f"{name}, a {description}, from {country}"

higherOrLower()
