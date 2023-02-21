import random
from words import word_list
from stages import hangman_stages


# pick a random word from the list
word = random.choice(word_list)

# set up the game
max_guesses = 6
current_guesses = 0
letters_guessed = []

# game loop
while current_guesses < max_guesses:
    # display the current state of the hangman
    print(hangman_stages[current_guesses])
    # display the current state of the word
    display_word = ''
    for letter in word:
        if letter in letters_guessed:
            display_word += letter
        else:
            display_word += '_'
    print(display_word)
    
    # get a guess from the player
    guess = input('Guess a letter: ').lower()
    
    # check if the guess is valid
    if len(guess) != 1 or not guess.isalpha():
        print('Please enter a single letter.')
        continue
    if guess in letters_guessed:
        print('You already guessed that letter.')
        continue
    
    # add the guess to the list of letters guessed
    letters_guessed.append(guess)
    
    # check if the guess is correct
    if guess in word:
        print('Correct!')
        if all(letter in letters_guessed for letter in word):
            print(f'You win! \n the word was {word}')
            break
    else:
        print('Incorrect.')
        current_guesses += 1
    
# end of game loop
if current_guesses == max_guesses:
    print(hangman_stages[current_guesses])
    print('You lose. \n The word was', word)
