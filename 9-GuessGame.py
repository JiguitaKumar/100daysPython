from random import randint

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.\n")
random = randint(1, 100)

easy_attempts = 10
hard_attempts = 5

def set_attempts(level):
    if level == "easy":
        return easy_attempts
    elif level == "hard":
        return hard_attempts
    else:
        print("Invalid input. Please try again.")
        return


def game_logic(target):

    level_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    
    if set_attempts(level_input) == None:
        return
    else:
        lives = set_attempts(level_input)
        print(f"You have {lives} attempts to guess the number.\n")

    while lives > 0:

        guess = int(input("Make a guess: "))

        if guess == target:
            print(f"You got it! The answer was {target}.")
            return
        elif guess > target:
            lives -= 1
            print(f"Too high. \nGuess again. \nYou have {lives} attempt(s) remaining to guess the number. \n")
        elif guess < target:
            lives -= 1
            print(f"Too low. \nGuess again. \nYou have {lives} attempt(s) remaining to guess the number. \n")
    
    print(f"You've run out of guesses. The answer was {target}.")
    return

game_logic(random)
