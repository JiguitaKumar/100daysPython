from random import randint

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
random = randint(1, 100)

easy_attempts = 10
hard_attempts = 5

def set_attempts(level):
    if level == "easy":
        print(f"You have {easy_attempts} attempts to guess the number.")
        return easy_attempts
    elif level == "hard":
        print(f"You have {hard_attempts} attempts to guess the number.")
        return hard_attempts
    else:
        print("Invalid input. Please try again.")
        exit()


def game_logic(target):

    level_input = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    lives = set_attempts(level_input)

    while lives > 0:

        guess = int(input("Make a guess: "))

        if guess == target:
            print(f"You got it! The answer was {target}.")
            exit()
        elif guess > target:
            lives -= 1
            print(f"Too high. \nGuess again. \nYou have {lives} attempt(s) remaining to guess the number. \n")
        elif guess < target:
            lives -= 1
            print(f"Too low. \nGuess again. \nYou have {lives} attempt(s) remaining to guess the number. \n")
    
    print(f"You've run out of guesses. The answer was {target}.")
    exit()

game_logic(random)
