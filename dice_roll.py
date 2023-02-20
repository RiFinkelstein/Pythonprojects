import random
import time

roll_again = "yes"

while roll_again == "yes":
    print("\n Rolling the dice...")
    time.sleep(1)
    dice_one = random.randint(1, 6)
    dice_two = random.randint(1, 6)
    print(
        f"The numbers you have rolled are:\nDice 1: {dice_one}\nDice 2: {dice_two}")
    if dice_one == dice_two:
        print("Sorry, try again!")
    else:
        print("Yayyy you win!")
    roll_again = input(
        "Do you want to play again? (Enter 'yes' to continue): ").lower()
