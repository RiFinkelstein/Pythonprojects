#in this code user guesses a number between 1 and 9 and if he guesses not in that range then it doesnt count it in the number of guesses
import random

number = random.randint(1, 9)
number_of_guesses = 0
while True:
	guess = int(input("Guess a number between 1 and 9: "))
	if guess== number:
		break
	elif guess >=1 and guess<=9:
		number_of_guesses += 1
		if guess > number:
            		print("Try again, a little lower.")
        	elif guess < number:
            		print("Try again, a little higher.")
	elif guess<1 or guess>9:
		print("choose a number between 1 and 9")

print(f"You needed {number_of_guesses} guesses to guess the number {number}")
