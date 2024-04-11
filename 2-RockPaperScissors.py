rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

user = input(
    "What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if int(user) == 0:
    print("User: Rock")
    print(rock)
elif int(user) == 1:
    print("User: Paper")
    print(paper)
elif int(user) == 2:
    print("User: Scissors")
    print(scissors)
else:
    print("Please choose a valid option.")

computer = random.randint(0, 2)
if int(computer) == 0:
    print("Computer: Rock")
    print(rock)
elif int(computer) == 1:
    print("Computer: Paper")
    print(paper)
elif int(computer) == 2:
    print("Computer: Scissors")
    print(scissors)

if computer == int(user):
    print("It is a tie!")
elif (computer == 0 and int(user) == 2) or (
        computer == 1 and int(user) == 0) or (computer == 2 and int(user) == 1):
    print("You lost!")
else:
    print("You WON!")
