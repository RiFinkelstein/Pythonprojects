import random

random_number = random.randint(1, 9)

guess = 0
count = 0

while guess != random_number:
    guess = int(input("enter a number between 1 and 9: "))
    count += 1
    if guess > random_number:
        print("nope, go lower")
    elif guess < random_number:
        print("nope,higher")
    else:
        print("correct")
        print(f"you took {count} tries")
