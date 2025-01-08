from random import randint

print("Welcome to the Number Guessing Game! \nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

random = randint(1, 100)

if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
else:
    print("Invalid input. Please try again.")
    exit()

print(f"You have {attempts} attempts remaining to guess the number.")

def game_logic(lives, target):

    while lives > 0:

        guess = int(input("Make a guess: "))

        if guess == target:
            print(f"You got it! The answer was {target}.")
            exit()
        elif guess > target:
            lives -= 1
            print(f"Too high. \nGuess again. \nYou have {lives} attempts remaining to guess the number. \n")
        elif guess < target:
            lives -= 1
            print(f"Too low. \nGuess again. \nYou have {lives} attempts remaining to guess the number. \n")
    
    print(f"You've run out of guesses. The answer was {target}.")
    exit()

game_logic(attempts, random)
