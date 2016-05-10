# One-Roll Dice
import random

users_guess=int(input("Guess the roll of the dice"))
number=random.randrange(1,7)
print("Roll is: ", number)
if number==users_guess:
    print("You win!!!!")

