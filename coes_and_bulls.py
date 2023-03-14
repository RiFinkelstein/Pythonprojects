import random

# Generate a random 4-digit number
number = str(random.randint(1000, 9999))

# Keep track of the number of guesses
num_guesses = 0

# Start the game loop
while True:
    # Prompt the user to enter a guess
    guess = input("Guess a 4-digit number: ")

    # Keep track of the number of cows and bulls
    num_cows = 0
    num_bulls = 0

    # Check each digit in the guess
    for i in range(4):
        if guess[i] == number[i]:
            num_cows += 1
        elif guess[i] in number:
            num_bulls += 1

    # Print the number of cows and bulls
    print(num_cows, "cows,", num_bulls, "bulls")

    # Increment the number of guesses
    num_guesses += 1

    # Check if the user has won
    if num_cows == 4:
        print("Congratulations, you guessed the number in",
              num_guesses, "guesses!")
        break
