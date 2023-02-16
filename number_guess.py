import random

random_number = random.randint(1, 9)

guess = int(input("enter a number: "))

if guess == random_number:
    print("yayy!! you won!!")
if guess > random_number:
    print("nope, go lower")
if guess < random_number:
    print("nope,higher")
