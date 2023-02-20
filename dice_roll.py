import random
import time


roll_again = "yes"

while roll_again == "yes":
    print("\nrolling te dice...")
    time.sleep(1)
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    print(
        f"the numbers you have rolled are: \n dice 1: {dice_one} \n dice 2: {dice_two}")
    if dice_one == dice_two:
        print("sorry, try again!")
    else:
        print("yayyy you win")
    roll_again = input("do you want to play again?: ")
